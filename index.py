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
                circle(20,360)
            elif g[l][c] ==1:
                up()
                goto(50*c,50*l)
                down()
                rond_rouge()
            elif g[l][c]==2:
                up()
                goto(50*c,50*l)
                down()
                rond_jaune()
        print("\n",end="")
#Place un rond jaune     
def rond_jaune():
    fillcolor('yellow')
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
    print(g[5][c])
    if g[5][c] == ".":
        return True
    else:
        return False
#Faire Jouer
def jouer(g,j,c):
    
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


# Variable Test
g = [[1,3,4,5,4,7], [1,".",".",4,5,4], [1,4,6,1,4,5], [1,".",".",4,5,4], [1,".",".",4,5,4], [1,".",".",4,5,4]]
        
print(coup_possible(g,1))




