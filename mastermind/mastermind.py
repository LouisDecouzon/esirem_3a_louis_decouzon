import random as rd

colours=["r","g","b","y","p","w"] # red, green, blue, yellow, purple, white
length_of_combination=4
def combination_to_guess(length:int): #returns a string 
    l=""
    for i in range(length):
        l+=(rd.choice(colours))
    return l

tries=1
partial=0
correct=0
c=combination_to_guess(length_of_combination)
print(c)
while tries!=12:
    g=str(input("Pls input a combination, for instance rgrp "))
    if g==c:
        print("you won in "+str(tries))
        break
    for i in g:
        if i in c:
            partial+=1
    for i in range(length_of_combination):
        if g[i]==c[i]:
            correct+=1
            partial-=1
    print("correct: "+str(correct)+"\n"+"partial: "+str(partial))
    tries+=1
