import os
import cv2
import numpy as np
from tqdm import tqdm
from config import DATA_DIR, IMG_SIZE

def count_images(data_dir):
    images = {}
    classes = os.listdir(data_dir)
    
    for class_name in classes:
        class_path = os.path.join(data_dir, class_name)
        images[class_name] = len(os.listdir(class_path))
        
    return images