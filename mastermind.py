import random as rd


length=4
list_of_colours=["red","green","blue","yellow","brown","orange","black","white"]
def list_to_guess(length:int):
    l=[]
    remaining_colours=list_of_colours.copy()
    for i in range(length):
        a=rd.choice(remaining_colours)
        l.append(a)
        remaining_colours.remove(a)
    print(l)
    return l

objective=list_to_guess(length)


def guess_input():
        guess=[]
        for i in range(length):
            iterative_guess= str(input("entrez une couleur "))
            guess.append(iterative_guess)
            #print(guess)
        return guess

turn=0
while turn!= 12:
    a=guess_input()
    if a==objective:
        print("vous avez gagné la manche")
        break
    print(a)

    bb=0
    for i in a:
        if i in objective:
            bb+=1

    br=0
    for u in range(length):
         if objective[u]==a[u]:
            br+=1
            bb-=1
    print("nombre de couleurs mal placées ",bb)
    print("nombre de couleurs bien placées ",br)
    turn+=1

if turn==12:
    print("vous avez perdu la manche")