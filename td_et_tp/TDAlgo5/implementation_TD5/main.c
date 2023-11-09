#include <stdio.h>
#include <stdlib.h>
// liste simplement chainee d'entiers
struct Noeud {
    int donnee;
    struct Noeud* suivant;
};

// Structure de la liste chaînee
struct ListeChainee {
    struct Noeud* tete;
};

// Structure du nœud de la liste doublement chaînée
struct Noeud2 {
    char caractere;
    struct Noeud2* precedent;
    struct Noeud2* suivant;
};

// Structure de la liste doublement chaînée
struct ListeDoubleChainee {
    struct Noeud2* tete;
    struct Noeud2* queue;
};
int somme_liste(struct ListeChainee* liste){
    int somme=0;
    struct Noeud* courant = liste->tete;
    while (courant!=NULL){
        somme=somme+courant->donnee;
        courant=courant->suivant;
    }
    return somme;
}

int produit_liste(struct ListeChainee* liste){
    int produit=1;
    struct Noeud* courant =liste->tete;
    while (courant!=NULL){
        produit=produit*courant->donnee;
        courant=courant->suivant;

    }
    return produit;
}

// Fonction pour trouver le maximum des éléments de la liste chaînée
int trouver_maximum(struct ListeChainee* liste) {
    int maximum = INT_MIN;

    struct Noeud* courant = liste->tete;

    while (courant != NULL) {
        if (courant->donnee > maximum) {
            maximum = courant->donnee;
        }
        courant = courant->suivant;
    }

    return maximum;
}
// Fonction pour trouver le maximum des éléments de la liste chaînée
int trouver_minimum(struct ListeChainee* liste){
    int minimum=INT_MAX;
    struct Noeud* courant =liste->tete;
    while (courant!=NULL){
        if(courant->donnee <minimum){
            minimum=courant->donnee;
        }
        courant = courant->suivant;
    }
    return minimum;
}

// Fonction pour trouver l'indice du maximum des éléments de la liste chaînée
int indice_du_max(struct ListeChainee* liste){
    int maximum=INT_MIN;
    int compteur =0;
    int indice_maximum=-1;
    struct Noeud* courant =liste->tete;
    while(courant!=NULL){
        if (courant->donnee>maximum){
            maximum=courant->donnee;
            indice_maximum=compteur;
        }
        courant=courant->suivant;
        compteur=compteur+1;
    }
    return compteur;
}
int main() {
    // Initialisation de la liste chaînée vide
    struct ListeChainee ma_liste;
    ma_liste.tete = NULL;

    // Initialisation de la liste doublement chainee vide
    struct ListeDoubleChainee ma_liste2;
    ma_liste2.tete = NULL;
    ma_liste2.queue = NULL;

    return 0;
}