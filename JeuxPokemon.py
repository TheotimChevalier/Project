'''
Created on 21 févr. 2023

@author: Me
'''
import time

class Jeux:
    def __init__(self, nomDeFichier):
        self.nomDeFichier = nomDeFichier

    
    def menu(self):
       
        
        message = ' Joueur 1 affronte Joueur 2'
        print('+' * (len(message)+4))
        print('+', message, '+')
        print('+' * (len(message)+4))
        choix = int(input("Saisissez 0 pour Choisir Pokemon \nSaisissez 1 pour prendre la fuite\n"))
         
        if choix == 0:
            self.choix0()
         
        elif choix == 1:
            self.choix1()
    
    def choix0(self):
        nom_poke = ['Carapuce', 'Salamesh', 'Bulbizare',
                    'Pikatchu', 'Ratata', 'Roucoups']
        pv_poke = [48, 49, 46, 50, 45, 47]
        
        print("J1, Choisissez votre pokemon parmi la liste suivante: ")
        for i in range(0, 6, 1):
            print("-", nom_poke[i])
        pokemon1 = int(input(""))-1.
        print()
        print(nom_poke[int(pokemon1)], " à été sélectionné.")
        PV1 = pv_poke[int(pokemon1)]
        
        print("J2, Choisissez votre pokemon parmi la liste suivante: ")
        for i in range(0, 6, 1):
            print("-", nom_poke[i])
        pokemon2 = int(input(""))-1
        print()
        print(nom_poke[int(pokemon2)], " à été sélectionné.")
        PV2 = pv_poke[int(pokemon2)]
        print()
        
        
        attaque_Salamesh = ['Flammèche', 'Machouille', 'Flame', 'Noyade']
        degat_Salamesh = [7, 5, 2, 8]
        
        attaque_Carapuce = ['Pistolet à eau',
                            'Groz\'yeux', 'Guillotine', 'Morsure']
        degat_Carapuce = [7, 2, 8, 5]
        
        attaque_Bulbizare = ['Fouet cuir végétal',
                              'Vampi\'graine', 'Plantage', 'Vive attaque']
        degat_Bulbizare = [7, 6, 4, 5]
        
        attaque_Pikatchu = ['Eclair', 'Encore', 'Analization', 'Miroire']
        degat_Pikatchu = [7, 3, 8, 4]
        
        attaque_Ratata = ['Charge', 'Griffe', 'Ecrasement', 'Netorare']
        degat_Ratata = [6, 1, 6, 9]
        
        attaque_Roucoups = ['Cru-aile',
                               'Jet de fumée', 'Sifflement', 'Regard']
        degat_Roucoups = [7, 5, 5, 5]
        
        choix_poke = [attaque_Carapuce, attaque_Salamesh, attaque_Bulbizare,
                      attaque_Pikatchu, attaque_Ratata, attaque_Roucoups]
        choix_attack = [degat_Carapuce, degat_Salamesh, degat_Bulbizare,
                        degat_Pikatchu, degat_Ratata, degat_Roucoups]
        
        
        def attack(n, v, m):
            print(choix_poke[int(n)])
            print()
            attaque_ref = 5
            while not (attaque_ref > -1 and attaque_ref < 4):
                attaque_ref = int(
                    input("Quelle attaque doit effectuer "+nom_poke[int(n)]+"? ")) - 1
                if attaque_ref <= -1:
                    print('Pas une attaque')
                elif attaque_ref > 4:
                    print('Pas une attaque')
            print()
            degat = choix_attack[int(n)][attaque_ref]
            v = max(v-degat, 0)
        
            fight = nom_poke[int(n)] + ' utilise ' + \
                choix_poke[int(n)][attaque_ref] + \
                ' qui inflige ' + str(degat) + ' PV'
            resultat = nom_poke[int(m)] + ' a maintenant ' + str(v) + ' PV'
            max_taille = max(len(fight), len(resultat))
            fight += ' ' * (max_taille - len(fight))
            resultat += ' ' * (max_taille - len(resultat))
            print('+'*(max_taille+4))
            print('+', fight, '+')
            print('+', resultat, '+')
            print('+'*(max_taille+4))
            print()
            return v
        
        
        def fin_combat(n, m, v):
            end1 = nom_poke[int(n)] + ' a été mis KO '
            print('+'*(len(end1)+4))
            print('+', end1, '+')
            print('+'*(len(end1)+4))
            print()
        
            msg_fin = 'résultat du combat : '
            fin2 = nom_poke[int(m)] + ' a gagner ce combat'
            fin1 = nom_poke[int(m)] + ' a fini avec ' + str(v) + ' HP'
            max_fin = max(len(fin2), len(msg_fin))
            msg_fin += ' ' * (max_fin - len(msg_fin))
            fin2 += ' ' * (max_fin - len(fin2))
            fin1 += ' ' * (max_fin - len(fin1))
            print('+'*(max_fin+4))
            print('+', msg_fin, '+')
            print('+', fin2, '+')
            print('+', fin1, '+')
            print('+'*(max_fin+4))
            print()
        
        
        start = nom_poke[int(pokemon1)] + ' (' + str(PV1) + ' PV) affronte ' + \
            nom_poke[int(pokemon2)] + ' (' + str(PV2) + ' PV)'
        print('+' * (len(start)+4))
        print('+', start, '+')
        print('+' * (len(start)+4))
        print()
        
        ok = input("Confirmez-vous ce duel? [o/n] ").lower()
        while not (ok == 'o' or ok == 'n'):
            print("t'as un choix parmi 2 possibilités et t'es pas foutu de le faire...")
            print()
            ok = input("Confirmez-vous ce duel? [o/n] ").lower()
        
        if ok == 'o':
            while PV2 > 0 and PV1 > 0:
                PV2 = attack(pokemon1, PV2, pokemon2)
                if PV2 <= 0:
                    break
                PV1 = attack(pokemon2, PV1, pokemon1)
        
                endt1 = nom_poke[int(pokemon1)] + ' a maintenant ' + str(PV1) + ' HP'
                endt2 = nom_poke[int(pokemon2)] + ' a maintenant ' + str(PV2) + ' HP'
                msg = 'résultat du tour : '
                max_end = max(len(endt1), len(endt2), len(msg))
                print('+'*(max_end+5))
                print('+', msg, ' '*(max_end-(len(msg))), '+')
                print('+', endt1, ' '*(max_end-(len(endt1))), '+')
                print('+', endt2, ' '*(max_end-(len(endt2))), '+')
                print('+'*(max_end+5))
                print()
        
            if PV1 <= 0:
                fin_combat(pokemon1, pokemon2, PV2)
        
            elif PV2 <= 0:
                fin_combat(pokemon2, pokemon1, PV1)

        self.menu()
    
    def choix1(self):
        print('vous prenez la fuite')
        self.menu()
        
        
        
jeux = Jeux("file1.txt")       
jeux.menu()
