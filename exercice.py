#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import turtle

def calcul_ellipsoide(a:float, b:float, c:float, masse_volumique: float) -> tuple:
    volume = 4/3 * math.pi * a * b * c
    return volume, volume * masse_volumique

# def arbre_recursivité():
#     turtle.
# fonction qui cherche si la chaine nest pas null et si elle contient seulement des a t c g
def chaine_valide(chaine: str):


# TODO: Définissez vos fonction ici

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(calcul_ellipsoide(4,5,6,7))
