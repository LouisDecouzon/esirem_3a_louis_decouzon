#include <stdio.h> /*tout le temps*/
#include <stdbool.h> /*pour utiliser des booleens*/


bool n_premier(int n){
    bool premier=1;
    if(n==2){
    premier=1;
    }
    else if (n==1){
    premier=0;
    }
    else{
        for(int i=2;i<n;i++){
            if (n%i==0){
                premier=0;
            }
        }
    }
    return premier;
}


void generer_premiersV1(int n){
    int compteur = 1;
    int compteur_de_np = 0;
    if (n > 0){
        while (compteur_de_np < n) {
            if (n_premier(compteur)) {
                printf("%d\n", compteur);
                compteur_de_np++;
            }
            compteur++;
        }
    }
    else if(n<=0){
        printf("%s","Probleme de bornes");
    }
}

void generere_premiersV2(int Mi,int Ma){
    int compteur= Mi;
    if (Ma>Mi){
        while(compteur<=Ma){
            if(n_premier(compteur)){
                printf("%d\n",compteur);
            }
            compteur++;
        }
    }
    else if (Ma<Mi){
        printf("%s","Probleme de bornes");

    }
}


int main(){
    //printf("%d",n_premier(73));
    //generer_premiersV1(54);
    //generer_premiersV2(5,17);
}