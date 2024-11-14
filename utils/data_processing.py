import os
import cv2
import numpy as np
from tqdm import tqdm
from config import DATA_DIR, IMG_SIZE

def load_images(data_dir):
    images, labels = [], []
    classes = os.listdir(data_dir)
    
    for label, class_name in enumerate(classes):
        class_path = os.path.join(data_dir, class_name)
        for img_name in tqdm(os.listdir(class_path), desc=f"Chargement {class_name}", unit="image"):
            img_path = os.path.join(class_path, img_name)
            img = cv2.imread(img_path)
            img = cv2.resize(img, IMG_SIZE)
            images.append(img)
            labels.append(label)
    
    images = np.array(images) / 255.0  # Normalisation
    labels = np.array(labels)
    return images, labels, class_name

def load_classes(data_dir):
    classes = os.listdir(data_dir)
    return classes