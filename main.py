import argparse
from scripts.train_model import train_model 
from scripts.real_time_detection import real_time_detection


def main():
    """Fonction principale du programme."""
    parser = argparse.ArgumentParser(description="Reconnaissance de portes")
    parser.add_argument('--train', action='store_true', help="Entraîner le modèle")
    parser.add_argument('--detect', action='store_true', help="Lancer la détection en temps réel")
    args = parser.parse_args()
    
    if args.train:
        train_model()
    elif args.detect:
        real_time_detection()
    else:
        print("Utilisez --train pour entraîner le modèle ou --detect pour lancer la détection en temps réel.")

if __name__ == "__main__":
    main()