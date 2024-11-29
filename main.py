import argparse
from scripts.train_model import train_model 
from scripts.real_time_detection import real_time_detection_heatmap, real_time_detection

def main():
    """Fonction principale du programme."""
    parser = argparse.ArgumentParser(description="Reconnaissance de portes")
    parser.add_argument('--train', action='store_true', help="Entraîner le modèle")
    parser.add_argument('--detect', action='store_true', help="Lancer la détection en temps réel")
    parser.add_argument('--heatmap', action='store_true', help="Lancer la détection en temps réel avec GradCAM")
    args = parser.parse_args()
    
    if args.train:
        train_model()
    elif args.detect:
        real_time_detection()
    elif args.heatmap:
        real_time_detection_heatmap()
    else:
        print("Utilisez --train pour entraîner le modèle, --detect pour la détection, ou --heatmap pour la détection avec GradCAM.")

if __name__ == "__main__":
    main()