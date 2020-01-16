#Puissance 4
from random import randint
from turtle import *

#Crée une grille vide
def grille_vide():
    return [[0]*7 for i in range(6)]

def grille_grise(g):
    for l in range(6):
        for c in range(7):
            carre_gris(c,l)

#Affiche la grille
def affiche(g):
    for l in range(6):
        for c in range(7):
            if g[l][c] ==1:
                carre_blanc(c,l)
                rond_bleu(c,l)
            elif g[l][c]==2:
                carre_blanc(c,l)
                rond_rouge(c,l)
        
#Place un rond bleu
                
def carre_blanc(c,l):
    up()
    goto(50*c,50*l)
    down()
    fillcolor('white')
    begin_fill()
    backward(20)
    for i in range(4):
        forward(40)
        left(90)
    end_fill()

def rond_bleu(c,l):
    up()
    goto(50*c,50*l)
    down()
    fillcolor('blue')
    begin_fill()
    circle(20,360)
    end_fill()

def carre_gris(c,l):
    up()
    goto(50*c,50*l)
    down()
    fillcolor('grey')
    begin_fill()
    backward(20)
    for i in range(4):
        forward(40)
        left(90)
    end_fill()

#place un rond rouge
def rond_rouge(c,l):
    up()
    goto(50*c,50*l)
    down()
    fillcolor('red')
    begin_fill()
    circle(20,360)
    end_fill()
    
#coup possible
def coup_possible(g,c):
    if c >= 1 and c <=7:
        c -= 1   
        if g[5][c] == 0:
            return True
        else:
            return False
    else:
        return False

#Jouer
def jouer(g,j,c):    
    l=0
    while g[l][c-1] != 0:
        l +=1
    g[l][c-1] = j  
                
    #Horizontale
def horiz(g,j,l,c):
    if c < 4:
        if g[l][c] == j and g[l][c+1]== j and g[l][c+2]== j and g[l][c+3]== j:
            return True
    
#verticale
def vert(g,j,l,c):
    if l < 3:
        if g[l][c] == j and g[l+1][c]== j and g[l+2][c]== j and g[l+3][c]== j:
            return True
    
#diagonale haut                
def diag_haut(g,j,l,c):
    if l < 3 and c < 4:
        if g[l][c] == j and g[l+1][c+1]== j and g[l+2][c+2]== j and g[l+3][c+3]== j:
            return True
    
#diagonale bas 
def diag_bas(g,j,l,c):
    if l > 2 and c < 4:
        if g[l][c] == j and g[l-1][c+1]== j and g[l-2][c+2]== j and g[l-3][c+3]== j:
            return True
    
#victoire     
def victoire(g,j):
    for l in range(6):
        for c in range(7):
            if horiz(g,j,l,c)==True or vert(g,j,l,c)==True or diag_haut(g,j,l,c)==True or diag_bas(g,j,l,c)==True:
                return True   
            
#match nul       
def match_nul(g,j):
    for c in range(7):
        if g[5][c]==0:
            return False
        
#coup joueur       
def coup_joueur(g,j):
    c=int(numinput(("joueur",j),"entrez une colonne : "))
    while coup_possible(g,c) == False:
        print("coup impossible !")
        c=int(numinput(("joueur",j),"entrez une colonne : "))
        
    jouer(g,j,c)
        
            
    
#programme principal
speed(0)
g=grille_vide()
grille_grise(g)
j=2
while victoire(g,j) != True and match_nul(g,j)==False:
    j=3-j
    coup_joueur(g,j)
    affiche(g)
    
print("victoire du joueur",j,"!")
