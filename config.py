import os

# Chemins des dossiers
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
MODELS_DIR = os.path.join(BASE_DIR, 'models')

# Hyperparamètres
IMG_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 10
LEARNING_RATE = 0.001

# Chemin pour sauvegarder le modèle
MODEL_SAVE_PATH = os.path.join(MODELS_DIR, 'door_recognition_model_3.h5')