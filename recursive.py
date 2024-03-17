def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


number = 3
print(f"La factoriel du nombre {number} est : {factorial(number)}")


def ask_choice_user(min_value, max_value):
    response_str = input(f"Veuillez choisir entre {min_value} et {max_value} : ")
    try:
        response_int = int(response_str)
        if min_value <= response_int <= max_value:
            return response_int
        else:
            print(f"Erreur : Veuillez entrer une valeur valide entre {min_value} et {max_value}")
            return ask_choice_user(min_value, max_value)  # Appel récursif pour demander une nouvelle saisie
    except ValueError:
        print("Erreur : Vous devez entrer un nombre")
        return ask_choice_user(min_value, max_value)  # Appel récursif en cas d'entrée invalide


choice = ask_choice_user(1, 4)
print("Choix de l'utilisateur : ", choice)
