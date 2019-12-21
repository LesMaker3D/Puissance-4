#Puissance 4
from random import randint
from turtle import *

#Crée une grille vide
def grille_vide():
    return [[0]*7 for i in range(6)]

#Affiche la grille
def affiche(g):
    clear()
    speed(0
    for l in range(6):
        for c in range(7):
            if g[l][c] ==0:
                up()
                goto(50*c,50*l)
                down()
                carrer_gris()
            elif g[l][c] ==1:
                up()
                goto(50*c,50*l)
                down()
                rond_bleu()
            elif g[l][c]==2:
                up()
                goto(50*c,50*l)
                down()
                rond_rouge()
        
#Place un rond bleu
def rond_bleu():
    fillcolor('blue')
    begin_fill()
    circle(20,360)
    end_fill()

def carrer_gris():
    fillcolor('grey')
    begin_fill()
    backward(20)
    for i in range(4):
        forward(40)
        left(90)
    end_fill()

#place un rond rouge
def rond_rouge():
    fillcolor('red')
    begin_fill()
    circle(20,360)
    end_fill()

 #

def coup_possible(g,c):
    c -= 1
   
    if g[5][c] == 0:
        return True

#Jouer
def jouer(g,j,c):

    o=0
    while g[o][c-1] != 0 or o > 6:
        o +=1
    g[o][c-1] = j
            
            
            
                    


#Horizontale
def horiz(g,j,l,c):
    if c < 4: 
        if g[l][c] == j and g[l][c+1]== j and g[l][c+2]== j and g[l][c+3]== j:
            return True


def vert(g,j,l,c):
    if l < 3:
        if g[l][c] == j and g[l+1][c]== j and g[l+2][c]== j and g[l+3][c]== j:
            return True
                
def diag_haut(g,j,l,c):
    if l < 3:
        if g[l][c] == j and g[l+1][c+1]== j and g[l+2][c+2]== j and g[l+3][c+3]== j:
            return True
    
def diag_bas(g,j,l,c):
    if l > 2:
        if g[l][c] == j and g[l-1][c-1]== j and g[l-2][c-2]== j and g[l-3][c-3]== j:
            return True
        
def victoire(g,j):
    return False
       
        
def match_nul(g,j):
    for c in range(7):
        if g[5][c]==0:
            return False
        
def coup_joueur(g,j):
    c=int(input("entrez une colonne : "))
    while coup_possible(g,c) == False or c < 1 or c > 7:
        print("Coup impossible !")
        c=int(input("entrez une colonne : "))
    jouer(g,j,c)


g=grille_vide()
affiche(g)
j=1
while victoire(g,j) == False and match_nul(g,j)==False:
    coup_joueur(g,j)
    affiche(g)
    j=3-j
