from tensorflow.keras.models import load_model
from config import MODEL_SAVE_PATH, DATA_DIR
from scripts.real_time_detection import real_time_detection

from utils.data_processing import load_images
from utils.analyse_data import count_images

# images, labels, class_name = load_images(DATA_DIR)

# print(images.shape)
# print(labels.shape)
# print(class_name)
# print(class_name.len())

print(count_images(DATA_DIR))