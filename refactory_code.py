def get_display_info_person(person_number):
    while True:
        try:
            ask_info_name = input("Quel est votre nom ? ")
            if not ask_info_name:
                raise ValueError("Le nom ne peut pas être vide.")
            if any(char.isdigit() for char in ask_info_name):
                raise ValueError("Le nom ne peut pas contenir de chiffres.")

            ask_info_age = input("Quel est votre âge ? ")
            if not ask_info_age.isdigit() or int(ask_info_age) <= 0:
                raise ValueError("L'âge doit être un nombre positif.")

            print(f"La personne {person_number} est {ask_info_name}, âgée de {ask_info_age} ans.")
            print(f"Le nom comporte : {len(ask_info_name)} caractères")
            break
        except ValueError as e:
            print(f"Erreur : {e}. Veuillez entrer des informations valides.")
    print("\nFin de programme !")


nb_person = 1
for i in range(nb_person):
    get_display_info_person(i + 1)
