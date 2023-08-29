# Tirage au sort d'un prix entre 1 et 10 (compris)
import random as rd
Prix = rd.randint(1, 32)
X = 0

def verif(Prix_param, X_param):
    # Message "Bravo" si le prix est trouvé
    if X_param == Prix_param:
        print("BRAVO !!!")
        return 0
    # Message "PAS ASSEZ ELEVEE" si le prix est rop bas
    elif X_param < Prix_param:
        print("PAS ASSEZ ELEVE")
    # Message "TROP ELEVE" si le prix est trop haut
    else:
        print("TROP ELEVE")
    return 1

if __name__ == '__main__':

    for i in range(5):
        # Choix du prix du joueur
        try:
            X = int(input(f"essai n°{i+1}, choisissez un entier entre 1 et 32 compris"))
        except ValueError:
            print("La valeur est incorrecte")
            continue   # Redemarre à l'itération suivante
        if verif(Prix,X) == 0: break
    # Message "PERDU" au bout de 5 essais
    if X != Prix:
        print("PERDU")
    # Fin au bout de 5 essais ou si le prix est trouvé
