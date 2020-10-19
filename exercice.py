#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
from turtle import setpos, back, forward, left, right

MAX_DEPTH = 4
BRANCH_LENGTH = 100
SHRINK_FACTOR = 0.8
TURN_ANGLE = 20 # degrees
def calcul_ellipsoide(a:float, b:float, c:float, masse_volumique: float) -> tuple:
    volume = 4/3 * math.pi * a * b * c
    return volume, volume * masse_volumique
def draw_trunk(BRANCH_LENGTH: int) -> None:
    left(90)
    penup()
    setpos(x = 0, y= -200)
    pendown()
    forward(BRANCH_LENGTH)

def draw_left(depth: int, distance:float)-> None:
    left(TURN_ANGLE)
    forward(distance * SHRINK_FACTOR)

    draw_tree(depth + 1)

    back(distance * SHRINK_FACTOR)
    right(TURN_ANGLE)

def draw_right(depth: int, distance:float)-> None:
    right(TURN_ANGLE)
    forward(distance * SHRINK_FACTOR)

    draw_tree(depth + 1)

    back(distance * SHRINK_FACTOR)
    left(TURN_ANGLE)

def draw_tree(depth:int) -> None:
    distance = BRANCH_LENGTH * SHRINK_FACTOR ** depth

    if depth <= MAX_DEPTH: #quand on arrive au bout
        draw_left(depth, distance)
        draw_right(depth, distance)
    


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
