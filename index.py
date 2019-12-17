#Puissance 4
from random import randint
from turtle import *


def grille_vide():
    g=[[0]*7]*6
    return g


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
        
def rond_jaune():
    fillcolor('yellow')
    begin_fill()
    circle(20,360)
    end_fill()

def rond_rouge():
    fillcolor('red')
    begin_fill()
    circle(20,360)
    end_fill()
    
    
# test
# affiche(grille_vide())
#g=[[0,1,0,1,0,1,0],[1,2,1,2,1,2,1],[0,1,0,1,0,1,0],[1,2,1,2,1,2,1],[0,1,0,1,0,1,0],[1,2,1,2,1,2,1]]




def coup_possible(g,c):
    c -= 1
    print(g[5][c])
    if g[5][c] == ".":
        return True
    else:
        return False



g = [[1,3,4,5,4,7], [1,".",".",4,5,4], [1,4,6,1,4,5], [1,".",".",4,5,4], [1,".",".",4,5,4], [1,".",".",4,5,4]]
        
print(coup_possible(g,1))




