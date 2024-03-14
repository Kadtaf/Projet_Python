import random
import time


def afficher_nombre_aleatoire(nombre):
    """Affiche un nombre aléatoire de 4 chiffres pendant 3 secondes."""
    print(nombre, end='', flush=True)  # Affiche le nombre
    time.sleep(3)  # Attend pendant 3 secondes
    print("\r" + " " * len(str(nombre)), end='', flush=True)  # Efface le nombre affiché


score = 0
sequence_length = 4
nombres_utilises = set()

while True:
    nombre_aleatoire = random.randint(10 ** (sequence_length - 1), (10 ** sequence_length) - 1)
    while nombre_aleatoire in nombres_utilises:
        nombre_aleatoire = random.randint(10 ** (sequence_length - 1), (10 ** sequence_length) - 1)
    nombres_utilises.add(nombre_aleatoire)
    print(nombres_utilises)

    # Demandez à l'utilisateur de retenir le nombre
    print("\nVous avez 3 secondes pour mémoriser le nombre qui s'affiche...")
    # Affiche le nombre aléatoire pendant 3 secondes
    time.sleep(1)  # Attend pendant 3 secondes
    afficher_nombre_aleatoire(nombre_aleatoire)

    while True:
        # Demandez à l'utilisateur d'écrire le nombre qu'il a mémorisé
        nombre_entre = input("\nEntrez le nombre que vous avez mémorisé : ")
        try:
            nombre_entre = int(nombre_entre)
            break
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    # Vérifie si le nombre entré par l'utilisateur correspond au nombre aléatoire
    if nombre_entre == nombre_aleatoire:
        print(f"Félicitations! Vous avez bien mémorisé le nombre.")
        score += 1
        sequence_length += 1
    else:
        print(
            f"Désolé,Mauvaise réponse , le nombre entré ne correspond pas au nombre affiché qui est : "
            f"{nombre_aleatoire} \n Votre score est : {score}")
        print("Fin de jeu")
        break
