import time
import beepy


def display_remaining_time(minutes, seconds):
    """Affiche le temps restant avec un format spécifique: MM:SS"""
    print("\nRemaining Time: {:02}:{:02}.....".format(minutes, seconds), end='', flush=True)


def cooking_timer(duration_minutes, use_sound):
    """Lance une minuterie de cuisson."""
    duration_seconds = duration_minutes * 60

    for remaining_seconds in range(duration_seconds, 0, -1):
        if remaining_seconds % 10 == 0:
            display_remaining_time(remaining_seconds // 60, remaining_seconds % 60)
        else:
            print(".", end='', flush=True)
        time.sleep(1)

    print("\n Cuisson términée")
    if use_sound:
        beepy.beep(sound=1)


# Affichage de menu
def choose_option():
    """Permet à l'utilisateur de choisir une option."""
    print("Options:")
    print("1. Oeufs à la coque (3 minutes)")
    print("2. Oeufs mollets (6 minutes)")
    print("3. Oeufs durs (9 minutes)")

    while True:
        choice = input("Choisissez une option (1, 2, ou 3) : ")
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("ERREUR : Veuillez entrez une valeur valide !")


def main():
    option = choose_option()

    if option == 1:
        cooking_duration = 1
    elif option == 2:
        cooking_duration = 6
    elif option == 3:
        cooking_duration = 9
    else:
        print("Option non valide. Veuillez choisir entre 1, 2 ou 3.")
        return

    print("\n Lancement de la cuisson des œufs...")
    cooking_timer(cooking_duration, use_sound=True)


if __name__ == "__main__":
    main()
