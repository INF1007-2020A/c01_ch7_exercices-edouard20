#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
from turtle import setpos, back, forward, left, right

def calcul_ellipsoide(a:float, b:float, c:float, masse_volumique: float) -> tuple:
    volume = 4/3 * math.pi * a * b * c
    return volume, volume * masse_volumique
def draw_trunk(BRANCH_LENGTH: int) -> None:
    left(90)
    penup()
    setpos(x = 0, y= -200)
    pendown()
    forward(BRANCH_LENGTH)

def arbre_recursivite(branches_to_draw: int):
    draw_trunk(10)
    while branches_to_draw > 0:
        turtle.forward(5)
        branches_to_draw -= 1
        arbre_recursivite(branches_to_draw)
    


#     turtle.
# fonction qui cherche si la chaine nest pas null et si elle contient seulement des a t c g
def chaine_valide(chaine: str):
    saisies_valides = ['a','t','g','c']
    if chaine == None:
        return False
    for i in range(len(chaine)):
        if chaine[i] not in saisies_valides[j]:
            return False
    return True
#def chaine_saisie(chaine: str):

def calculer_proportion(chaine: str, seq:str):
   occurences =  chaine.count(seq)
   return_string = f"Il y a {round((occurences/len(chaine))* 100, 2)} % de {seq}"
   return return_string


# TODO: Définissez vos fonction ici

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(calcul_ellipsoide(4,5,6,7))
    print(calculer_proportion('attgcaatggtggtacatg','ca'))
    print(arbre_recursivite(8))
