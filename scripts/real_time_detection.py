import cv2
from config import IMG_SIZE, DATA_DIR, MODEL_SAVE_PATH
import numpy as np
from utils.data_processing import load_classes
from utils.display_info import display_info
from tensorflow.keras.models import load_model # type: ignore
from utils.Grad_Cam import generate_gradcam, overlay_heatmap

def real_time_detection():
    """Fonction pour la détection en temps réel."""
    print("Chargement du modèle pour la détection...")
    model = load_model(MODEL_SAVE_PATH)
    
    # Charger les classes
    class_names = load_classes(DATA_DIR)
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Erreur : Impossible d'accéder à la webcam.")
        return

    print("Détection en temps réel activée. Appuyez sur 'q' pour quitter.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Prétraiter l'image pour la prédiction
        img = cv2.resize(frame, IMG_SIZE)
        img = np.expand_dims(img, axis=0) / 255.0

        # Prédire la porte
        predictions = model.predict(img)
        class_idx = np.argmax(predictions)
        label = class_names[class_idx]

        # Afficher le label sur l'image
        cv2.putText(frame, f"Local: {label}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Afficher des informations supplémentaires
        display_info(label)

        # Afficher la vidéo en direct
        cv2.imshow("Door Recognition", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def real_time_detection_heatmap():
    """Fonction pour la détection en temps réel avec GradCAM."""
    model = load_model(MODEL_SAVE_PATH)

    # Charger les classes
    class_names = load_classes(DATA_DIR)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Prétraiter l'image pour la prédiction
        img = cv2.resize(frame, IMG_SIZE)
        img = np.expand_dims(img, axis=0) / 255.0

        # Prédire la porte
        predictions = model.predict(img)
        class_idx = np.argmax(predictions)
        label = class_names[class_idx]

        # Générer la carte GradCAM
        heatmap = generate_gradcam(model, img[0], class_idx, layer_name='Conv_1')

        # Superposer la carte de chaleur sur l'image originale
        heatmap_overlay = overlay_heatmap(heatmap, frame)

        # Afficher le label et les informations
        cv2.putText(heatmap_overlay, f"Local: {label}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        display_info(label)

        # Afficher la vidéo en direct avec GradCAM
        cv2.imshow("Door Recognition with GradCAM", heatmap_overlay)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()