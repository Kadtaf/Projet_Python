import random
import time


def afficher_nombre_aleatoire(nombre):
    """Affiche un nombre aléatoire de 4 chiffres pendant 3 secondes."""
    print(nombre, end='', flush=True)
    time.sleep(3)
    print("\r" + " " * len(str(nombre)), end='', flush=True)  # Efface le nombre affiché


score = 0
sequence_length = 4

while True:
    nombre_aleatoire = random.randint(10 ** (sequence_length - 1), (10 ** sequence_length) - 1)
    nb = random.randint(0, 9)
    print("\nVous avez 3 secondes pour mémoriser le nombre qui s'affiche...")
    time.sleep(1)
    afficher_nombre_aleatoire(nombre_aleatoire)

    while True:
        nombre_entre = input("\nEntrez le nombre que vous avez mémorisé : ")
        try:
            nombre_entre = int(nombre_entre)
            break
        except ValueError:
            print("Veuillez entrer un nombre valide!")

    if nombre_entre == nombre_aleatoire:
        print(f"Félicitations! Vous avez bien mémorisé le nombre.")
        score += 1
        sequence_length += 1
    else:
        print(
            f"Désolé,Mauvaise réponse , le nombre entré ne correspond pas au nombre affiché qui est : "
            f"{nombre_aleatoire}")
        print(f"Fin de jeu \n Votre score est : {score}")
        exit()
