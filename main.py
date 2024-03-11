"""
#Méthode 1
POUCE = "inch"
CENTIMETRE = "cm"
ONE_INCH = 2.54


def ask_user():
    while True:
        ask_convers_user = input(f"Veuillez choisir le mode de conversion : {POUCE} ou {CENTIMETRE}? ").lower()
        if ask_convers_user in [POUCE, CENTIMETRE]:
            return ask_convers_user
        else:
            print("ERREUR : Choix invalide. Veuillez choisir entre 'inch' et 'cm'.")


def get_user_input(unit_str):
    while True:
        try:
            ask_nb_user = float(input(f"Veuillez entrer la valeur à convertir ({unit_str}): ").replace(',', '.'))
            return ask_nb_user
        except ValueError:
            print("ERREUR : Veuillez entrer une valeur numérique valide.")


def main():
    val_str = ask_user()

    while True:
        ask_nb_user = get_user_input(val_str)

        if val_str == POUCE:
            calcul_cm = ask_nb_user * ONE_INCH
            calcul_round = round(calcul_cm, 2)
            print(f"Résultat après conversion : {ask_nb_user} {val_str} = {calcul_round} {CENTIMETRE}")
        elif val_str == CENTIMETRE:
            calcul_pouce = ask_nb_user / ONE_INCH
            calcul_round = round(calcul_pouce, 2)
            print(f"Résultat après conversion : {ask_nb_user} {val_str} = {calcul_round} {POUCE}")

        continuer = input("Voulez-vous convertir une autre valeur ? (oui/non) ")
        if continuer.lower() != "oui":
            print("Fin du programme !")
            break


if __name__ == "__main__":
    main()
"""
# Méthode 2
POUCE = "inch"
CENTIMETRE = "cm"
ONE_INCH = 2.54


# Fonction pour demander à l'utilisateur de choisir l'unité de conversion
def ask_user():
    while True:
        ask_convers_user = input(f"Veuillez choisir le mode de conversion : {POUCE} ou {CENTIMETRE}? ").lower()
        if ask_convers_user in [POUCE, CENTIMETRE]:
            return ask_convers_user
        else:
            print("ERREUR : Choix invalide. Veuillez choisir entre 'inch' et 'cm'.")


# Fonction pour demander à l'utilisateur d'entrer une valeur à convertir
def get_user_input(unit_str):
    while True:
        try:
            ask_nb_user = float(input(f"Veuillez entrer la valeur à convertir ({unit_str}): ").replace(',', '.'))
            return ask_nb_user
        except ValueError:
            print("ERREUR : Veuillez entrer une valeur numérique valide.")


# Fonction pour effectuer la conversion
def convertir(valeur, unite_source, unite_cible):
    if unite_source == POUCE and unite_cible == CENTIMETRE:
        return valeur * ONE_INCH
    elif unite_source == CENTIMETRE and unite_cible == POUCE:
        return valeur / ONE_INCH


# Fonction pour afficher le résultat de la conversion
def afficher_resultat(valeur, unite_source, valeur_convertie, unite_cible):
    print(f"Résultat après conversion : {valeur} {unite_source} = {valeur_convertie} {unite_cible}")


# Fonction principale du programme
def main():
    # Demander à l'utilisateur de choisir l'unité de conversion
    unite_source = ask_user()

    while True:
        # Demander à l'utilisateur d'entrer la valeur à convertir
        valeur = get_user_input(unite_source)

        # Déterminer l'unité cible en fonction de l'unité source
        unite_cible = CENTIMETRE if unite_source == POUCE else POUCE

        # Effectuer la conversion
        valeur_convertie = convertir(valeur, unite_source, unite_cible)
        valeur_convertie_arrondie = round(valeur_convertie, 2)

        # Afficher le résultat
        afficher_resultat(valeur, unite_source, valeur_convertie_arrondie, unite_cible)

        # Demander à l'utilisateur s'il souhaite convertir une autre valeur
        continuer = input("Voulez-vous convertir une autre valeur ? (oui/non) ")
        if continuer.lower() != "oui":
            print("Fin du programme !")
            break


# Appel de la fonction main() pour exécuter le programme
if __name__ == "__main__":
    main()


"""
# effectuer_conversion : Cette fonction convertit les unités unit1 vers unit2

#Return :
 #True : L'utilisateur ne veut plus convertir (sortir du programme)
 #False : L'utilisateur a donné une valeur à convertir

def demander_et_afficher_conversion(unit1: str, unit2: str, facteur: float):
    valeur_str = input(f"Conversion {unit1} -> {unit2}. Donnez la valeur en {unit1} (ou 'q' pour quitter) : ")
    if valeur_str == "q":
        return True
    try:
        valeur_float = float(valeur_str)
    except ValueError:
        print("ERREUR : Vous devez rentrer une valeur numérique")
        print("(utilisez le point et non la virgule pour les décimales)")
        return demander_et_afficher_conversion(unit1, unit2, facteur)

    valeur_convertie = round(valeur_float * facteur, 2)
    print(f"Résultat de la conversion : {valeur_float} {unit1} = {valeur_convertie} {unit2}")
    return False


while True:
    # Menu : choix de la conversion
    print("Ce programme vous permet d'effectuer des conversions d'unités")
    print("1 - Pouces vers cm")
    print("2 - cm vers pouces")
    choix = input("Votre choix (1 ou 2): ")
    if choix == "1" or choix == "2":
        break
    print("ERREUR : Vous devez choisir 1 ou 2")

while True:
    # Demander les valeurs à convertir à l'utilisateur
    if choix == "1":
        if demander_et_afficher_conversion("pouces", "cm", 2.54):
            break
    if choix == "2":
        if demander_et_afficher_conversion("cm", "pouces", 0.394):
            break

"""
