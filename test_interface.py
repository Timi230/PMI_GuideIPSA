import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Bibliothèque Pillow pour redimensionner les images
import pandas as pd
import os
import webbrowser

def tkinter_windows(label):
    #rajouter lien,email,photo

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

    logo_path = "asset/" + label + ".png"
    
    for i, nom in enumerate(code_asso_col):
        if label == nom:
            index = i
            break

    # Création de la fenêtre principale
    root = tk.Tk()
    root.title("AI Powered Guide for IPSA")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.geometry(str(int(screen_width/2))+"x"+str(int(screen_height-100))+"+"+str(int(screen_width/2))+"+0")

    # Frame pour le header (logo + nom de l'association)
    header_frame = tk.Frame(root, bg="white", height=100)
    header_frame.pack(fill="x")

    # Chargement et redimensionnement du logo
    logo_image = Image.open(logo_path)  # Remplacez par le chemin de votre logo
    logo_image = logo_image.resize((150, 150))  # Taille réduite du logo
    logo = ImageTk.PhotoImage(logo_image)

    # Ajout du logo
    logo_label = tk.Label(header_frame, image=logo, bg="white")
    logo_label.pack(side="left", padx=10, pady=10)

    # Nom de l'association
    association_name = tk.Label(header_frame, text=nom_asso_col[index], font=("Arial", 20, "bold"), bg="white")
    association_name.pack(side="left", padx=20)

    # Frame pour la présentation 
    presentation_frame = tk.LabelFrame(root, text="Présentation de l'association",font=("Arial",10, "bold"), padx=10, pady=10, bd=5)
    presentation_frame.pack(fill="both", padx=10, pady=5)

    # Contenu de la présentation
    presentation_text = descriptif_col[index]

    presentation_label = tk.Label(presentation_frame, text=presentation_text, wraplength="600", font=("Arial", 12), justify="left", anchor="w")
    presentation_label.pack(fill="both", expand=True)

    ### Frame pour les projets main ###
    projects_main_frame = tk.LabelFrame(root, text="Projets phares",font=("Arial",10, "bold"), padx=10, pady=10, bd=5)
    projects_main_frame.pack(fill="x", padx=10, pady=5)

    # Liste des projets
    projects_main = projet_realise_col[index]

    project_label = tk.Label(projects_main_frame, text=projects_main,wraplength="600", font=("Arial", 12), justify="left", anchor="w")
    project_label.pack(anchor="w")

    ### Frame pour les projets en cours ###
    projects_now_frame = tk.LabelFrame(root, text="Projets en cours",font=("Arial",10, "bold"), padx=10, pady=10, bd=5)
    projects_now_frame.pack(fill="x", padx=10, pady=5)

    # Liste des projets
    projects_now = projet_en_cours_col[index]

    project_now_label = tk.Label(projects_now_frame, text=projects_now,wraplength="600", font=("Arial", 12), justify="left", anchor="w")
    project_now_label.pack(anchor="w")

    ### Frame pour les projets  ###
    reference_frame = tk.LabelFrame(root, text="Référent",font=("Arial",10, "bold"), padx=10, pady=10, bd=5)
    reference_frame.pack(fill="x", padx=10, pady=5)

    # Liste des projets
    reference_text = referents_col[index] + "\nEmail : " + email_col[index]

    reference_label = tk.Label(reference_frame, text=reference_text, cursor="hand2", wraplength="600",font=("Arial", 12), justify="left", anchor="w")
    reference_label.pack(anchor="w")
    reference_label.bind("<Button-1>", lambda e: ouvrir_email())

    # Boucle principale
    root.mainloop()

def ouvrir_email():
    # Ouvre le client de messagerie par défaut avec l'adresse email
    webbrowser.open("mailto:example@example.com")

label = "lab_scrypt_L020"
tkinter_windows(label)