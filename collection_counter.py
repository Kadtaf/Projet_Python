import time
import beepy


def display_remaining_time(minutes, secondes):
    """ Affiche le temps restant avec un format spécifique . MM:SS"""
    print("\nTemps restant : {:02}:{:02}.....".format(minutes, secondes), end='', flush=True)


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


def choose_option():
    """Permet à l'utilisateur de choisir une option."""

    options = {
        '1': {'title': "Oeufs à la coque", 'duration': 3},
        '2': {'title': "Oeufs mollets", 'duration': 3},
        '3': {'title': "Oeufs durs", 'duration': 3}
    }
    print("Options:")
    for key, value in options.items():
        print(f"{key}. {value['title']} ({value['duration']} minutes)")
    while True:
        choice = input("\n  Choisissez une option (1? 2, ou 3) : ")
        if choice in options:
            return options[choice]['duration']
        else:
            print("ERREUR : Veuillez entrer une valeur valide !")


def main():
    cooking_duration = choose_option()

    print("\nLancement de la cuisson des œufs...")
    cooking_timer(cooking_duration, use_sound=True)


if __name__ == "__main__":
    main()

