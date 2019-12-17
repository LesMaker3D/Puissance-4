#Puissance 4
from random import randint
from turtle import *

#Crée une grille vide
def grille_vide():
    g=[[0]*7]*6
    return g

#Affiche la grille
def affiche(g):
    speed(0)
    for l in range(6):
        for c in range(7):
            if g[l][c] == 0:
                up()
                goto(50*c,50*l)
                down()
                rond_gris()
            elif g[l][c] ==1:
                up()
                goto(50*c,50*l)
                down()
                rond_rouge()
            elif g[l][c]==2:
                up()
                goto(50*c,50*l)
                down()
                rond_bleu()
        print("\n",end="")
#Place un rond jaune     
def rond_bleu():
    fillcolor('blue')
    begin_fill()
    circle(20,360)
    end_fill()

def rond_gris():
    fillcolor('grey')
    begin_fill()
    circle(20,360)
    end_fill()

#place un rond rouge 
def rond_rouge():
    fillcolor('red')
    begin_fill()
    circle(20,360)
    end_fill()

 #Vérifie si le coup peut être jouer dans la colonne

def coup_possible(g,c):
    c -= 1
    if g[5][c] == 0:
        return True
    else:
        return False

#Terminer Jouer
def jouer(g,j,c):
    if coup_possible(g,c):

        for i in range(6):
            o = 5-i
            if g[o][c-1] == 0: 
                if j == 1:
                    g[o][c-1] = 1
                    print("C'est dans if J1")
                    print(g[o][c-1])
                else:
                    g[o][c-1] = 2
                    print("C'est dans if J2")
                    print(g[o][c-1])
    else:
        return "Pas jouable"
    return g
"""
#Faire Horiz
def horiz(g,j,l,c):

#Faire Vert
def vert(g,j,l,c):

#faire diag haut
def diag_haut(g,j,l,c):

#Faire diag bas

def diag_bas(g,j,l,c)

#Faire fonction victoire

def victoire(g,j):

#Faire fonction match nul

def math_nul(g,j):

#Faire Programme principale 
"""

# Variable Test
g=[[2,1,1,1,2,1,1],[1,2,2,2,1,2,1],[0,1,2,1,2,1,2],[1,2,1,2,1,2,1],[0,1,2,1,1,1,1],[0,2,0,0,1,2,0]]
        
print(jouer(g,1,3))




