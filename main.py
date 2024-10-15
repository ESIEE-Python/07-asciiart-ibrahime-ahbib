# ************* Module main

"""
Ce module contient deux fonctions qui permettent d'encoder une chaîne de caractères
en une liste de tuples. L'encodage est réalisé de manière itérative avec `artcode_i` 
et récursive avec `artcode_r`.
"""

# Importation des modules nécessaires
import sys

# Définition des variables globales
sys.setrecursionlimit(1200)

# Définition des fonctions

def artcode_i(s):
    """
    Retourne la liste de tuples encodant une chaîne de caractères passée en argument 
    selon un algorithme itératif.

    Args:
        s (str): la chaîne de caractères à encoder.

    Returns:
        list: la liste des tuples (caractère, nombre d'occurrences).
    """

    # Initialisation de la liste de tuples
    l_tuples = []
    # Initialisation du compteur
    count = 1

    for i in range(1, len(s)):
        # Si le caractère courant est identique au précédent
        if s[i] == s[i - 1]:
            # On incrémente le compteur
            count += 1
        else:
            # Sinon on ajoute le tuple (caractère, compteur) à la liste
            l_tuples.append((s[i - 1], count))
            # On réinitialise le compteur
            count = 1

    # On ajoute le dernier tuple
    l_tuples.append((s[-1], count))

    return l_tuples


def artcode_r(s):
    """
    Retourne la liste de tuples encodant une chaîne de caractères passée en argument 
    selon un algorithme récursif.

    Args:
        s (str): la chaîne de caractères à encoder.

    Returns:
        list: la liste des tuples (caractère, nombre d'occurrences).
    """

    # Cas de base
    if len(s) == 0:
        return []

    # Recherche du nombre de caractères identiques au premier
    count = 1
    while count < len(s) and s[count] == s[0]:
        count += 1

    # Retourne le premier tuple et continue récursivement
    return [(s[0], count)] + artcode_r(s[count:])


# Définition de la fonction principale

def main():
    """
    Fonction principale exécutant les tests d'encodage de chaînes de caractères
    en utilisant les deux algorithmes définis.
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))


# Point d'entrée du programme
if __name__ == "__main__":
    main()
