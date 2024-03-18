import os
import time


def process_data(big_data, callback):
    print("Traîtement de données en cours...... pour : ", big_data)
    time.sleep(2)
    print("Traîtement des données terminé pour :", big_data)
    callback()


def display_message():
    print("Le traîtement des données est terminé !")


data = [1, 2, 3, 4, 5]
process_data(data, display_message)
print()


def add_callback(a, b):
    return a + b


def subst_callback(a, b):
    return a - b


def divi_callback(a, b):
    if b != 0:
        return a / b
    else:
        print("Divison par zéro impossible !")
        return None


def mult_callback(a, b):
    return a * b


def power_callback(a, b):
    return pow(a, b)


def display_table(n, operator_str, operation_callback):
    for i in range(1, 10):
        print(i, operator_str, n, "=", operation_callback(i, n))


display_table(2, "x", mult_callback)
print()
display_table(2, "^", power_callback)
print()
display_table(2, "+", add_callback)


def add(title, **number):
    print("TITRE :", title)
    result = 0
    moyen = 0
    for n in number.values():
        result += n / len(number.values())
        moyen = round(result)
    return moyen


print(add("Moyenne des notes", math=12, Physique=23, Chimie=30))


def a(nom, age, taille: float = 0):
    print("Vous êtes " + nom)
    print("vous avez :" + str(age))
    if taille > 0:
        print("vous faite :" + str(taille))


a("Paule", 20)

a("Jean", 24, 1.5)


def f1(n):
    if n > 5:
        return
    ligne = ""
    for i in range(n):
        ligne += "#"
    print(ligne)
    f1(n + 1)


f1(1)
# -----------------Tuples------------------
person = ("Melanie", "Paule", "Jean", "Tamarra")
for i in person:
    print(i)
    print(len(i))
    print(i[-1])
# -------------------Listes-----------------------
personnes = ["Melanie", "Paule", "Jean", "Tamarra"]
print(personnes)
new_person = "Dawoud"
personnes.append(new_person)
print(personnes)
del personnes[1]
print(personnes)


def modify_value(b):
    b[0] = 1.4
    b[3] = 35
    b[2] = "Mathilde"
    b[1] = True


test = [1, 2, 3, 4]
print(test)
modify_value(test)
print(test)


# -----------Fonctions et Tuples------------
def get_info():
    return "Mathilde", 37, 1.68


def display_info(name, age, taille: float):
    print(f"Information: Nom: {name}, Âge: {age}, Taill: {taille}")


info = get_info()
display_info(*info)

# -----------------------------Exercice Liste---------------


n = 6
name = []
for i in range(n):
    name_person = input("Nom de la personne : ")
    if name_person == "":
        break
    name.append(name_person)
print(name)
print()
print("Noms des personnes : ")
for i in name:
    print(" ", i)

# ------------------------Exercice 2 Listes---------------------
driver_names = ["Paul", "Mathild", "Jack", "Mathieu", "Momo", "Karim", "Mamadou"]
mile_driver_km = [1.5, 2.2, 0.4, 0.9, 7.1, 1.1, 0.6]
# Algorithme V1
"""index_min = mile_driver_km.index(min(mile_driver_km))
mile_min = mile_driver_km[index_min]
driver_name = driver_names[index_min]


print(f"Distace minimale : {mile_min} km, Chauffeur : {driver_name}")
"""

# Algorithme V2

index_min = 0
mile_min = mile_driver_km[0]
for i in range(len(mile_driver_km)):
    mile = mile_driver_km[i]
    if mile < mile_min:
        mile_min = mile
        index_min = i
print(f"Distace minimale : {mile_min} km, Chauffeur : {driver_names[index_min]}")
