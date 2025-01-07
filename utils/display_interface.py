import tkinter as tk
from tkinter import messagebox
import pandas as pd
from PIL import Image, ImageTk
import webbrowser
import pyttsx3
import time

def lire_a_haute_voix(textes):
    """Lit une liste de textes à voix haute avec une gestion explicite des événements."""
    moteur = pyttsx3.init()  # Initialiser le moteur vocal
    moteur.connect('finished-utterance', on_utterance_finished)  # Connecter l'événement de fin de lecture
    
    try:
        for texte in textes:
            global utterance_done  # Variable pour suivre l'état de la lecture
            utterance_done = False  # Réinitialiser l'état
            moteur.say(texte)  # Ajouter le texte au moteur vocal
            moteur.runAndWait()  # Attendre que la lecture soit terminée
            
            # Attendre explicitement la fin de la lecture
            while not utterance_done:
                time.sleep(0.1)  # Petite pause pour réduire la charge CPU
    except Exception as e:
        print(f"Erreur lors de la synthèse vocale : {e}")
    finally:
        moteur.stop()  # Arrêter proprement le moteur vocal


def on_utterance_finished(name, completed):
    """Callback déclenché à la fin de la lecture d'un texte."""
    global utterance_done
    utterance_done = True

def display_interface(label):
    # Charger les données depuis le fichier Excel
    df = pd.read_excel("Info_Association.xlsx")

    # Accéder aux colonnes spécifiques
    nom_asso_col = df["Nom de l'asso"]
    projet_realise_col = df["Projet déjà réalisé"]
    feedback_proj_realise_col = df["Feedback - Projet déjà réalisé"]
    projet_en_cours_col = df["Projet en cours"]
    referents_col = df["Référents (NOM - Prénom)"]
    descriptif_col = df["Descriptif"]
    code_asso_col = df["Code asso"]
    email_col = df["email"]

    # Rechercher les associations correspondant au label
    indices = df[code_asso_col == label].index.tolist()
    

    if not indices:
        messagebox.showinfo("Aucune association", "Aucune association trouvée pour ce label.")
        return

    # Création de la fenêtre principale
    root = tk.Tk()
    root.title("AI Powered Guide for IPSA")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.geometry(str(int(screen_width / 2)) + "x" + str(int(screen_height - 100)) + "+" + str(int(screen_width / 2 - 10)) + "+0")

 # Créer un canvas et une barre de défilement verticale
    canvas = tk.Canvas(root)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview, width = 23)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    # Créer un frame pour contenir tout le contenu scrollable
    content_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    # Mettre à jour la barre de défilement lorsque le contenu change
    content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    i = 0
    images = []

    for i, index in enumerate(indices):
        association_frame = tk.LabelFrame(content_frame, text=f"Association {nom_asso_col[index]}", font=("Arial", 12, "bold"), padx=10, pady=10, bd=2)
        association_frame.pack(fill="x", padx=10, pady=10)

        if len(indices) == 1:
            logo_path = f"asset/{label}.png"
        else:
            logo_path = f"asset/{label}_{i}.png"
        
        try:
            logo_image = Image.open(logo_path)
            logo_image = logo_image.resize((150, 150))  
            logo = ImageTk.PhotoImage(logo_image)
            images.append(logo)
        except FileNotFoundError:
            logo = None
        
        i+=1

        header_asso_frame = tk.Frame(association_frame, bg="white", height=100)
        header_asso_frame.pack(fill="x")

        if logo:
            logo_label = tk.Label(header_asso_frame, image=logo, bg="white")
            logo_label.pack(side="left", padx=10, pady=10)

        association_name = tk.Label(header_asso_frame, text=nom_asso_col[index], font=("Arial", 20, "bold"), bg="white")
        association_name.pack(side="left", padx=20)

        # Présentation de l'association
        presentation_frame = tk.LabelFrame(association_frame, text="Présentation de l'association", font=("Arial", 10, "bold"), padx=10, pady=10, bd=5)
        presentation_frame.pack(fill="both", padx=10, pady=5)

        presentation_text = descriptif_col[index]
        presentation_label = tk.Label(presentation_frame, text=presentation_text, wraplength=600, font=("Arial", 12), justify="left", anchor="w")
        presentation_label.pack(fill="both", expand=True)

        # Projets réalisés
        projects_main_frame = tk.LabelFrame(association_frame, text="Projets phares", font=("Arial", 10, "bold"), padx=10, pady=10, bd=5)
        projects_main_frame.pack(fill="x", padx=10, pady=5)

        projects_main = projet_realise_col[index]
        project_label = tk.Label(projects_main_frame, text=projects_main, wraplength=600, font=("Arial", 12), justify="left", anchor="w")
        project_label.pack(anchor="w")

        # Projets en cours
        projects_now_frame = tk.LabelFrame(association_frame, text="Projets en cours", font=("Arial", 10, "bold"), padx=10, pady=10, bd=5)
        projects_now_frame.pack(fill="x", padx=10, pady=5)

        projects_now = projet_en_cours_col[index]
        project_now_label = tk.Label(projects_now_frame, text=projects_now, wraplength=600, font=("Arial", 12), justify="left", anchor="w")
        project_now_label.pack(anchor="w")

        # Référents
        reference_frame = tk.LabelFrame(association_frame, text="Référent", font=("Arial", 10, "bold"), padx=10, pady=10, bd=5)
        reference_frame.pack(fill="x", padx=10, pady=5)

        reference_text = referents_col[index] + "\nEmail : " + email_col[index]
        reference_label = tk.Label(reference_frame, text=reference_text, cursor="hand2", wraplength=600, font=("Arial", 12), justify="left", anchor="w")
        reference_label.pack(anchor="w")
        reference_label.bind("<Button-1>", lambda e: ouvrir_email())

        # Section Lecture audio
        audio_frame = tk.LabelFrame(association_frame, text="Lecture audio", font=("Arial", 10, "bold"), padx=10, pady=10, bd=5)
        audio_frame.pack(fill="x", padx=10, pady=5)

        # Texte à lire
        textes_a_lire = [
            f"Présentation de l'association : {presentation_text}",
            f"Projets phares : {projects_main}",
            f"Projets en cours : {projects_now}",
            f"Référents : {referents_col[index]}, Email : {email_col[index]}"
        ]

        # Bouton pour lire à haute voix
        lire_button = tk.Button(
            audio_frame,
            text="Lire à haute voix",
            command=lambda: lire_a_haute_voix(textes_a_lire),
            font=("Arial", 12),
            padx=10,
            pady=5,
            bg="#4CAF50",
            fg="white"
        )
        lire_button.pack(anchor="center")
    root.mainloop()

def ouvrir_email():
    webbrowser.open("mailto:example@example.com")



"""label = "aeroIPSA"
display_interface(label)"""