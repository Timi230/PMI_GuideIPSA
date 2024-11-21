from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
import tensorflow as tf
from config import DATA_DIR, EPOCHS, BATCH_SIZE, MODEL_SAVE_PATH, LEARNING_RATE

from utils.data_processing import load_images
from sklearn.model_selection import train_test_split

def train_model():
    
    images, labels, class_names = load_images(DATA_DIR)
    
    X_train, X_val, y_train, y_val = train_test_split(images, labels, test_size=0.2, random_state=42)
    
    # Charger le modèle MobileNetV2 pré-entraîné
    base_model = MobileNetV2(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
    base_model.trainable = False  # On gèle les couches pour utiliser les features pré-apprises

    # Ajouter des couches de classification
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(128, activation='relu')(x)
    
    output = Dense(len(class_names), activation='softmax')(x)

    model = Model(inputs=base_model.input, outputs=output)

    # Compiler le modèle
    model.compile(optimizer=Adam(learning_rate=LEARNING_RATE), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Entraîner le modèle
    model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=EPOCHS, batch_size=BATCH_SIZE)
        
    model.save(MODEL_SAVE_PATH)
    
    return model
