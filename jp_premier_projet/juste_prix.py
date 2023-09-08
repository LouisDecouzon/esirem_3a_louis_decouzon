import random as rd
import os 
ia=False
def gamemode():
    gm=str(input("Choose your gamemode i for infinite number of tries, or l for a limited one, or ia in order for the computer to guess the number "))
    if gm=="i":
        ia=False
        try_number=float('inf')
        wog=True
    elif gm=="ia":
        ia=True
        try_number=float('inf')
        wog=False
    else:
        ia=False
        try_number=7 # balanced for guessing between 1 and 100 
        wog=True
    return try_number,wog,ia

try_number,will_of_gaming,ia=gamemode()
mini=1
maxi=100
assert mini<maxi
def gen_nombre(borne_inf,borne_sup): #generates a random number between mini and maxi
    r=rd.randint(mini,maxi)
    return r
tries=0
loss=0
win=0
txt='Input a number between ',mini,'and',maxi,
game_starter='Input p to play, q to quit or r to reset '
txt_entry_error='Invalid number, please enter a number between',mini,'and',maxi
ingame=True
tg=gen_nombre(mini,maxi)
while ia==True:
    a,b=mini,maxi
    tn=1
    print(tg)
    cv=int((a+b)/2)
    if tg==cv:
        print("Found in"+tn)
        break
    if tg>cv:
        a=int((a+b)/2)
    if tg<cv:
        b=int((a+b)/2)
    tn+=1






while will_of_gaming==True:
    while ingame==True: #debut de la partie
        nbr=gen_nombre(mini,maxi)
        u=str(input(game_starter))
        tries=0
        while tries!=try_number: #debut de la manche
            tries+=1
            if u=='q': #choix de quitter, reset les stats ou de jouer 
                break
            if u=='r': #reset avant de jouer(tester) car les fichiers stats uploaded sur github ne sont pas vierges
                os.system("attrib -h jp_premier_projet\juste_prix_stat.txt") #montre le fichier
                stat=open("jp_premier_projet\juste_prix_stat.txt",'w') # ouvre puis referme le fichier, ce qui efface son contenu
                stat.close()
                os.system("attrib +h jp_premier_projet\juste_prix_stat.txt")#recache le fichier stat
                break
            else:
                n=int(input(txt)) # si on veut jouer, il faut entrer un nombre entre mini et maxi
                if n>maxi or n<mini:
                    n=int(input(txt_entry_error)) #donne une autre chance si on a rentre un nombre incorrect

            if n==nbr:
                print("You won in ",tries," tries")
                stat_jp=open("jp_premier_projet\juste_prix_stat.txt",'a')
                stat_jp.write("Won in "+str(tries)+"tries")
                stat_jp.write("\n")
                stat_jp.close() # ecrit l'historique des parties gagnees(nombre d'essais  avant de gagner)
                os.system("attrib +h jp_premier_projet\juste_prix_stat.txt") #+h to hide and -h to show + path of the file
                win+=1
                break
            if n>nbr:
                print("It is smaller")
            else:
                print("It is bigger")
            if tries==try_number:
                loss+=1
        print("Currently: computer:",loss," you:",win," Do you want to play another round?")
        replay=str(input("Type y if you want and n if you do not "))
        assert replay=="y" or "n"
        if replay=="n":
            ingame=False #fin de la manche
    r=str(input("Do you want to replay? y to yes, n to no "))
    if r=="n":
        will_of_gaming=False #fin de la partie 
    ingame=True
os.system("attrib -h jp_premier_projet\match_history.txt")
match_history=open("jp_premier_projet\match_history.txt","a")
match_history.write("Computer:"+str(loss)+" You:"+str(win))
match_history.write("\n")
match_history.close()
os.system("attrib +h jp_premier_projet\match_history.txt")