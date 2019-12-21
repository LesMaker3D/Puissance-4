#Puissance 4
from random import randint
from turtle import *

#Crée une grille vide
def grille_vide():
    return [[0]*7 for i in range(6)]

#Affiche la grille
def affiche(g):
    speed("fastest")
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
    else:
        return False

#Jouer
def jouer(g,j,c):
    for i in range(6):
        o = 5-i
        if g[o][c-1] == 0:
            g[o][c-1] = j
                    

                    print(g[o][c-1])
                else:
                    g[o][c-1] = 2
                    print("C'est dans if J2")
                    print(g[o][c-1])
    else:
        return "Pas jouable"
    return g

#Horizontale
def horiz(g,j):
    compteur = 0
    l = 0
    for i in range(6):
        for k in range(7):
            if g[i][k] == j:
                if l == i:
                    l = i
                compteur += 1
                if compteur == 4:
                    return "Victoire du joueur",j
            else:
                compteur = 0
#Horizontale V2 sans boucle
def horizv2(g,j,l,c):
        if g[l][c] == j and g[l][c-1]== j and g[l][c-2]== j and g[l][c-3]== j: # horizontal gauche
            return True
        elif g[l][c] == j and g[l][c+1]== j and g[l][c+2]== j and g[l][c+3]== j: #  horizontal droite
            return True
        else:
            return False
            

#Verticale
def vert(g,j):
    compteur = 0
    l = 0
    for i in range(6):
        for k in range(5):
            print("i:",i, "k",k)
            if g[k][i] == j:
                if l == i:
                    l = i
                    compteur += 1
                    print("compteur",compteur)
                if compteur == 4:
                    return True
            else:
                compteur = 0
                
#Verticale 2 sans boucle
def vert2(g,j,l,c):
        if g[l][c] == j and g[l-1][c]== j and g[l-2][c]== j and g[l-3][c]== j: # vertical bas
            return True
        elif g[l][c] == j and g[l+1][c]== j and g[l+2][c]== j and g[l+3][c]== j: #  vertical haut
            return True
        else:
            return False

#diagonale haut
def diag_haut(g,j,l,c):
    if l < 3:
        if g[l][c] == j and g[l+1][c-1]== j and g[l+2][c-2]== j and g[l+3][c-3]== j: # diagonales haut gauche
            return True
        elif g[l][c] == j and g[l+1][c+1]== j and g[l+2][c+2]== j and g[l+3][c+3]== j: # diagonales haut droite
            return True
        else:
            return False
    else:
            return False


# diag bas

def diag_bas(g,j,l,c):
    if l > 3:
        if g[l][c] == j and g[l-1][c-1]== j and g[l-2][c-2]== j and g[l-3][c-3]== j: # diagonales haut gauche
            return True
        elif g[l][c] == j and g[l-1][c+1]== j and g[l-2][c+2]== j and g[l-3][c+3]== j: # diagonales bas droite
            return True
        else:
            return False
    else:
            return False






#Faire fonction victoire

def victoire(g,j,l,c):
    if diag_bas(g,j,l,c):
        print("Félicitation vous avez gagné !1")
    elif diag_haut(g,j,l,c):
        print("Félicitation vous avez gagné !2")
    elif vert(g,j):
        print("Félicitation vous avez gagné !3")
    elif horiz(g,j):
        print("Félicitation vous avez gagné !4")

#Faire fonction match nul

def math_nul(g,j):
    compteur = 0
    for i in range(7):
        if coup_possible(g,i):
            compteur += 1
    if compteur == 7:
        print("Match Nul")


#Faire Programme principale


# Variable Test
g=[[1,1,0,1,1,2,1],[1,2,1,2,1,2,1],[1,2,1,2,1,2,1],[1,1,2,1,2,1,2],[2,1,2,1,2,1,2],[2,1,2,1,2,2,1]]

victoire(g,1,4,1)
affiche(g)



