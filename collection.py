# Définition des données de conversion pour chaque unité
CONVERSION_DATA = {
    "inch": {"display": "pouces", "factor": 2.54},
    "cm": {"display": "centimètres", "factor": 1 / 2.54}
}


# Fonction pour demander à l'utilisateur de choisir l'unité de conversion
def ask_user():
    while True:
        ask_convers_user = input(
            f"Veuillez choisir le mode de conversion : {CONVERSION_DATA['inch']['display']} ou "
            f"{CONVERSION_DATA['cm']['display']}? ").lower()
        if ask_convers_user in CONVERSION_DATA:
            return ask_convers_user
        else:
            print("ERREUR : Choix invalide. Veuillez choisir entre 'inch' et 'cm'.")


# Fonction pour demander à l'utilisateur d'entrer une valeur à convertir
def get_user_input(unit_str):
    while True:
        try:
            ask_nb_user = float(input(f"Veuillez entrer la valeur à convertir ("
                                      f"{unit_str}): ").replace(',', '.'))
            return ask_nb_user
        except ValueError:
            print("ERREUR : Veuillez entrer une valeur numérique valide.")


# Fonction pour effectuer la conversion
def convertir(valeur, unite_source):
    factor_source = CONVERSION_DATA[unite_source]["factor"]
    return valeur * factor_source


# Fonction pour afficher le résultat de la conversion
def afficher_resultat(valeur, unite_source, valeur_convertie, unite_cible):
    display_source = CONVERSION_DATA[unite_source]["display"]
    display_cible = CONVERSION_DATA[unite_cible]["display"]
    print(f"Résultat après conversion : {valeur} {display_source} = {valeur_convertie} {display_cible}")


# Fonction principale du programme
def main():
    # Demander à l'utilisateur de choisir l'unité de conversion
    unite_source = ask_user()

    while True:
        # Demander à l'utilisateur d'entrer la valeur à convertir
        valeur = get_user_input(CONVERSION_DATA[unite_source]["display"])

        # Déterminer l'unité cible en fonction de l'unité source
        unite_cible = "cm" if unite_source == "inch" else "inch"

        # Effectuer la conversion
        valeur_convertie = convertir(valeur, unite_source)
        valeur_convertie_arrondie = round(valeur_convertie, 2)

        # Afficher le résultat
        afficher_resultat(valeur, unite_source, valeur_convertie_arrondie, unite_cible)

        # Demander à l'utilisateur s'il souhaite convertir une autre valeur
        continuer = input("Voulez-vous convertir une autre valeur ? (oui/non) ")
        if continuer.lower() != "oui":
            print("Fin du programme !")
            break


# Appel de la fonction main() pour exécuter le programme
main()
