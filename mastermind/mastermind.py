import random as rd
import os

colours=["r","g","b","y","p","w"] # red, green, blue, yellow, purple, white
length_of_combination=4
def combination_to_guess(length:int): #returns a string 
    l=""
    for i in range(length):
        l+=(rd.choice(colours))
    return l

ingame=False
partial=0
correct=0
choice=str(input("Type p to play, q to quit or r to reset your statistics "))
if choice not in ["p","q","r"]:
    replay=str(input("Pls type either p, q or r"))

if choice=="p":
    ingame=True
if choice =="q":
    print("see you")
if choice =="r": # choosing to reset the statistics do not entail palying a game, hence nothing happens once stats are get reset
    os.system("attrib -h mastermind_game_number.txt")
    stat=open("mastermind_game_number.txt","w")
    stat.truncate()
    stat.write("0")
    stat.close()
    os.system("attrib +h mastermind_game_number.txt")


while ingame==True: #initial loop to begin to play a game of mastermind (find ONE code)
    c=combination_to_guess(length_of_combination)
    print(c)
    tries=1
    while tries!=12:
        g=str(input("Pls input a combination of r(red) g(greeg) b(blue) y(yellow) p(purple) w(white) , for instance rgrp "))
        if g==c:
            print("you won in "+str(tries)+" tries")
            break
        for i in g:
            if i in c:
                partial+=1
        for i in range(length_of_combination):
            if g[i]==c[i]:
                correct+=1
                partial-=1
        print("correct: "+str(correct)+"\n"+"partial: "+str(partial))
        partial,correct=0,0
        tries+=1
    # ajouter les stats ici
    game_number=os.system("attrib -h mastermind_game_number.txt")
    game_number=open("mastermind_game_number.txt","r+")
    gn=game_number.read()
    gn = int(gn)
    game_number.truncate(0)
    gn+=1
    game_number.write(str(gn))
    game_number.close()
    game_number=os.system("attrib +h mastermind_game_number.txt")

    replay=str(input("type p to play again, q to quit or r to reset your statistics "))
    if replay not in ["p","q","r"]:
        replay=str(input("pls enter either p, q or r "))
    if replay=="q":
        ingame=False
    

