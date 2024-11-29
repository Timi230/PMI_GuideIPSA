import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model

def generate_gradcam(model, image, class_index, layer_name='Conv_1'):
    """
    Génère une carte GradCAM pour une image donnée.
    
    Args:
        model: Modèle entraîné.
        image: Image d'entrée de dimension (224, 224, 3).
        class_index: Index de la classe cible.
        layer_name: Nom de la couche convo pour GradCAM.
    
    Returns:
        heatmap: Carte de chaleur GradCAM redimensionnée à la taille de l'image.
    """
    grad_model = tf.keras.models.Model(
        [model.inputs], [model.get_layer(layer_name).output, model.output]
    )

    # Traçage du gradient
    with tf.GradientTape() as tape:
        conv_outputs, predictions = grad_model(tf.expand_dims(image, axis=0))
        loss = predictions[:, class_index]

    # Calcul des gradients
    grads = tape.gradient(loss, conv_outputs)
    weights = tf.reduce_mean(grads, axis=(0, 1, 2))  # Moyenne pondérée des gradients
    conv_outputs = conv_outputs[0]

    # Pondération des activations par les gradients
    heatmap = tf.reduce_sum(weights * conv_outputs, axis=-1).numpy()

    # Appliquer ReLU pour ne conserver que les activations positives
    heatmap = np.maximum(heatmap, 0)
    heatmap /= np.max(heatmap)  # Normaliser entre 0 et 1

    # Redimensionner la carte de chaleur à la taille de l'image
    heatmap = cv2.resize(heatmap, (image.shape[1], image.shape[0]))

    return heatmap

def overlay_heatmap(heatmap, image, alpha=0.4):
    """
    Superpose une carte de chaleur sur l'image originale.
    
    Args:
        heatmap: Carte de chaleur (normalisée entre 0 et 1).
        image: Image originale.
        alpha: Facteur de transparence de la superposition.
    
    Returns:
        superimposed_img: Image avec la carte de chaleur superposée.
    """
    # Vérifier si l'image est en niveaux de gris et la convertir en BGR
    if len(image.shape) == 2 or image.shape[2] == 1:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    # Redimensionner la carte de chaleur pour qu'elle corresponde à la taille de l'image
    heatmap = cv2.resize(heatmap, (image.shape[1], image.shape[0]))

    # Normaliser la carte de chaleur entre 0 et 255, puis appliquer une coloration
    heatmap = np.uint8(255 * heatmap)
    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)

    print("Heatmap shape:", heatmap.shape)
    print("Image shape:", image.shape)


    # Superposer la carte de chaleur sur l'image originale
    superimposed_img = cv2.addWeighted(image, 1 - alpha, heatmap, alpha, 0)
    return superimposed_img
