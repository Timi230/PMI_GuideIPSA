import os

# Dictionnaire de correspondance pour convertir les labels des dossiers
label_mapping = {
    "aeroipsa": "aeroIPSA",
    #"aeroRC": "aeroRC",
    #"amphi_LO17": "amphi_LO17",
    "bd_kart_airsoft_dreamage_B005": "bd_kart_airsoft_dreamage_B005",
    "bde": "bde",
    #"bdj_B003": "bdj_B003",
    #"bds_B002": "bds_B002",
    #"corridor": "corridor",
    "flight": "flight",
    "Itech_B002": "Itech_B002",
    #"lab_drone_L015": "lab_drone_L015",
    #"lab_elec_L021": "lab_elec_L021",
    #"lab_elec2_L021": "lab_elec2_L021",
    #"lab_L018A": "lab_L018A",
    #"lab_L018B": "lab_L018B",
    #"lab_LEMA_L024": "lab_LEMA_L024",
    "lab_scrypt_L020": "lab_scrypt_L020",
    "lab_scrypt2_L020": "lab_scrypt_L020"
    #"lab_thermo_L018C": "lab_thermo_L018C"
}

def convert_label_from_folder(folder_name):
    """
    Convertit un nom de dossier en son label correspondant dans Excel.

    :param folder_name: str - Nom du dossier (label brut)
    :return: str - Label correspondant ou message d'erreur si non trouvé
    """
    return label_mapping.get(folder_name, f"Erreur : {folder_name} n'a pas de correspondance valide.")

"""
def process_folders_in_directory(directory_path):
    
    Parcourt les dossiers d'un répertoire et convertit chaque nom en label Excel.

    :param directory_path: str - Chemin du répertoire contenant les dossiers
    :return: dict - Dictionnaire des labels convertis
    
    if not os.path.isdir(directory_path):
        return f"Erreur : Le chemin '{directory_path}' n'est pas un répertoire valide."

    # Parcourir les dossiers dans le répertoire
    folder_names = [folder for folder in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, folder))]
    
    # Convertir chaque label en son équivalent Excel
    converted_labels = {folder: convert_label_from_folder(folder) for folder in folder_names}
    
    return converted_labels
"""