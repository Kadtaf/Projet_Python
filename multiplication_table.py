def multiplication_tables(n, min=1, max=9):
    if min < 1 or max < 1:
        raise ValueError("Les valeurs min et max doivent être supérieures ou égales à 1")
    if min > max:
        raise ValueError("La valeur min ne doit pas être supérieur à la valeur max")

    for i in range(min, max + 1):
        print(f"{i} x {n} = {i * n}")
    print(f"-------------Fin de la table de : {n} ---------------------")

try:
    multiplication_tables(6)
except ValueError as e:
    print(f"Erreur: {e}")
