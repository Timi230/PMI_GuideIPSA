def display_info(label):
    """Affiche des informations sur le local en fonction du label."""
    info = {
        "lab_drone_L015": "Laboratoire de drones - Projets en cours : Recherche IA, Optimisation de vol.",
        "aeroipsa": "les fusée c'est cool",
    }
    
    if label in info:
        print(f"Information sur {label}: {info[label]}")
    else:
        print("Local inconnu.")