from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request
from pydantic import BaseModel
import shutil
import os


from tensorflow.keras.models import load_model
from utils.data_processing import load_classes
from config import IMG_SIZE, DATA_DIR, MODEL_SAVE_PATH
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import pandas as pd


app = FastAPI()
app.mount("/static", StaticFiles(directory="webApp/static"), name="static")

# Permettre les requêtes CORS pour le frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Charger le modèle et les classes au démarrage du serveur
print("Chargement du modèle et des classes...")
model = load_model(MODEL_SAVE_PATH)
class_names = load_classes(DATA_DIR)
print(class_names)

associations_data = {}


# Modèle pour l'ID envoyé depuis le frontend
class AssociationRequest(BaseModel):
    id: str
    

@app.on_event("startup")
async def load_association_data():
    global associations_data
    # Charger les données depuis le fichier Excel
    df = pd.read_excel("Info_Association.xlsx")

    # Créer un dictionnaire pour chaque association
    for _, row in df.iterrows():
        associations_data[row["Code asso"]] = {
            "name": row["Nom de l'asso"],
            "main_projects": row["Projet déjà réalisé"],
            "current_projects": row["Projet en cours"],
            "referent": row["Référents (NOM - Prénom)"],
            "presentation": row["Descriptif"],
            "email": row["email"], 
            "logo": row["Logo_web"],
        }

    print(f"{len(associations_data)} associations chargées.")

# Endpoint pour afficher l'index (page principale)
@app.get("/", response_class=FileResponse)
async def get_index():
    return FileResponse("webApp/index.html")


@app.post("/process-image/")
async def process_image(file: UploadFile = File(...)):
    """
    Endpoint pour traiter une image envoyée depuis le frontend et retourner le nom de l'association.
    """
    # Charger l'image envoyée
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Prétraiter l'image pour la prédiction
    img = cv2.resize(frame, IMG_SIZE)
    img = np.expand_dims(img, axis=0) / 255.0

    # Prédire la porte
    predictions = model.predict(img)
    class_idx = np.argmax(predictions)
    label = class_names[class_idx]
    print(label)
    return {"label": label}

@app.get("/get-association-info/{code_asso}")
async def get_association_info(code_asso: str):
    if code_asso not in associations_data:
        return {'name': '', 'main_projects': "Pas encore d'informations ...", 'current_projects': "Pas encore d'informations ...", 'referent': "Pas encore d'informations ...", 'presentation': "Pas encore d'informations ...", 'email': "Pas encore d'informations ...", 'logo': '/static/images/ipsa_bg.png'}
    print(associations_data[code_asso])
    return associations_data[code_asso]
