# Tirage au sort d'un prix entre 1 et 10 (compris)
import random as rd
Prix = rd.randint(1, 10)
X = 0
for i in range(5):
    # Choix du prix du joueur
    try:
        X = int(input(f"essai n°{i+1}, choisissez un entier entre 1 et 10 compris"))
    except ValueError:
        print("La valeur est incorrecte")
        continue   # Redemarre à l'itération suivante
    # Message "BRAVO" si le prix est trouvé
    if X == Prix:
        print("BRAVO !!!")
        break
    # Message "PAS ASSEZ ELEVEE" si le prix est rop bas
    elif X < Prix:
        print("PAS ASSEZ ELEVE")
    # Message "TROP ELEVE" si le prix est trop haut
    else:
        print("TROP ELEVE")
# Message "PERDU" au bout de 5 essais
if X != Prix:
    print("PERDU")
# Fin au bout de 5 essais ou si le prix est trouvé
