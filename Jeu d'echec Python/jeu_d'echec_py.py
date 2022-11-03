# -*- coding: utf-8 -*-
"""Jeu d'echec.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15fHOW4RtMDtF17VyG7ldMIGVQ-v64lk9
"""

"""

Programme réalisé par GUNDUZ Maxime

Vous pouvez tester directement le code en cliquant sur le lien ci-dessous:
https://colab.research.google.com/drive/15fHOW4RtMDtF17VyG7ldMIGVQ-v64lk9?usp=sharing

Code disponible sur mon Github: 

https://colab.

"""

from random import randint

#VALEUR INITIAL

jouer=True
point_p1=0
point_p2=0
tour=0 
coup=["Q","P","F","C"]

# MAIN
while jouer :
    
    #CHOIX MACHINE
    player2=randint(1,3)
    player2=coup[player2]

    #CHOIX HUMAIN
    player1=-5
    while 0>player1 or player1>5:
        player1=int(input(print("-QUITTER (0)\n\n-Pierre (1)\n-Feuille (2)\n-Cisseau (3)\n\nQue choissisez vous ?")))
    player1=coup[player1]
    
    #CONDITION QUITTER
    if player1=="Q":
        jouer=False
        print("FIN DE LA PARTI")
        print("\nVOTRE SCORE : ",point_p1,"\nSCORE DE LA MACHINE : ", point_p2,"\n")
        if point_p1>point_p2:
            print("VOUS AVEZ GAGNER !")
        elif point_p2>point_p1:
            print("VOUS AVEZ PERDU !")
        else:
            print("MATCH NULL")
        break
    
    #CONDITION SUR LES DIFFERENTS CAS 
    if (player1=="P" and player2=="C") or (player1=="F" and player2=="P") or (player1=="C" and player2=="F"):
        point_p1+=1
        print("\nVous avez gagner")
        
    elif (player1=="C" and player2=="P") or (player1=="F" and player2=="C") or (player1=="P" and player2=="F"):
        point_p2+=1
        print("\nVous avez Perdu")
        
    else:
        print("\nEGALITE")
    
    #AFFICHAGE TABLEAU DE JOUEUR
    tour+=1
    print("################# TOUR ",tour," #################")
    print("#################################################")
    print("||   JOUEUR 1(Vous)    ||    JOUEUR 2 MACHINE  ||")
    print("||---------------------------------------------||")
    print("||         ",point_p1,"         ||          ",point_p2,"         ||")
    print("||---------------------------------------------||")
    print("#################################################")