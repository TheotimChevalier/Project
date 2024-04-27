import random 
import time as t
import pygame
import pickle

def Rejouer():
    mamamia = pygame.mixer.Sound('Super Mario 64 Mamma mia.mp3')
    R = str(input("Voulez-vous rejouer ? (1: Oui, 2: Non) : "))       
    if R == '1' or R == 'o':
        R = True
        return R
    else:
        t.sleep(0.5)
        print("Très bien...")
        t.sleep(1)
        print("Je...")
        t.sleep(1.5)
        print("Je comprends...")
        t.sleep(1)
        print("À Bientôt !")
        pygame.mixer.music.stop()
        pygame.mixer.init()
        pygame.mixer.music.load('Mario Death - Sound Effect (HD).mp3')
        pygame.mixer.music.play()
        t.sleep(3)
        mamamia.play()
        print("Snif...")
        t.sleep(1)
        
# Sauvegarder le jeu
def sauvegarder_jeu(maze, entry_x, entry_y, x, y, exit_x, exit_y, min_x, min_y, star_x, star_y, portal_a_x, portal_a_y, portal_b_x, portal_b_y, level, score, minaumort):
    etat_jeu = {
        "maze": maze,
        "entry_x": entry_x,
        "entry_y": entry_y,
        "x": x,
        "y": y,
        "exit_x": exit_x, 
        "exit_y": exit_y,
        "min_x": min_x,
        "min_y": min_y,
        "star_x" : star_x,
        "star_y": star_y, 
        "portal_a_x": portal_a_x, 
        "portal_a_y": portal_a_y,
        "portal_b_x": portal_b_x,
        "portal_b_y": portal_b_y,
        "level": level, 
        "score": score,
        "minaumort": minaumort
    }
    with open("sauvegarde_jeu.pickle", "wb") as fichier:
        pickle.dump(etat_jeu, fichier)
        
  
def Laby(maze2 = None, entry_x = None, entry_y=None, x=None, y=None, exit_x=None, exit_y=None, min_x=None, min_y=None, star_x=None, star_y=None, portal_a_x = None, portal_a_y = None, portal_b_x = None, portal_b_y = None, level = None, score = None,minaumort=None):
    
    WALL = "\033[1;34mX\033[0m"
    PATH = " "
    ENTRY = "E"
    EXIT = "S"
    PORTAL = "\033[1;32mP\033[0m"
    STAR = "\033[1;33mx\033[0m"
    TRAIL ="."
    MIN = "\033[1;31mM\033[0m"
    
    if not level :
        level = int(input("Choisissez votre niveau : 1 ou 2 : "))
    
    pygame.mixer.init()
    pipe = pygame.mixer.Sound('pipe.mp3')
    champi = pygame.mixer.Sound('champi.mp3')
    boup = pygame.mixer.Sound('boup.mp3')
    pygame.mixer.music.load('Super-Mario-Bros.-Theme-Song.wav')
    pygame.mixer.music.play()
    
    
    # Définition des variables
    size = 10  # Taille du labyrinthe (10x10)
    if maze2 :
        maze = maze2
    else: 
        maze = [[WALL if random.randint(0, 2) == 0 or x == 0 or x == size - 1 or y == 0 or y == size - 1 else PATH for x in range(size)] for y in range(size)] # Création du labyrinthe
    
    temps1 = t.time()  
    if score == None :
        if level == 2 :
            score = 20
        else : 
            score = 25
    
    
    # Placement de l'entrée
    if entry_x == None and entry_y == None:
        entry_x, entry_y = random.randint(1, size), random.randint(0, 0)
        # exit_x, exit_y = random.randint(1, size - 1), random.randint(0, size - 1)
        maze[entry_x][entry_y] = ENTRY

    if exit_x == None and exit_y == None : 
        if level == 1 :
            #Placement de la sortie
            exit_x, exit_y = random.randint(1, size - 1), random.randint(0, size - 1)
            maze[size - 1][random.randint(1, size - 2)] = EXIT
            minaumort = "OK" #Pour éviter un placement infini de la sortie du au True en bas


    #definition de x et y
    if x == None and y== None :
        x, y = entry_x, entry_y
    
    # Vérifictation de si on peut sortir de l'entrée
  #  while maze[y+1] and maze[y+1] and maze[x-1][y+1] and maze[x+1][y + 1]!= WALL:
       # maze = [[WALL if random.randint(0, 2) == 0 or x == 0 or x == size - 1 or y == 0 or y == size - 1 else PATH for x in range(size)] for y in range(size)] # Création du labyrinthe
        # Placement de l'entrée et de la sortie
        #entry_x, entry_y = random.randint(1, size), random.randint(0, 0)
        #exit_x, exit_y = random.randint(1, size - 1), random.randint(0, size - 1)
    
   # maze[entry_x][entry_y] = ENTRY
    #maze[size - 1][random.randint(1, size - 2)] = EXIT


    
 
    # Placement des portails
    if portal_a_x == None and portal_a_y == None and portal_b_x == None and portal_b_y == None:
        num_portals = random.randint(1, 3)  # Nombre de portails à placer
        for i in range(num_portals):
            portal_a_x, portal_a_y = random.randint(1, size - 2), random.randint(1, size - 2)
            portal_b_x, portal_b_y = random.randint(1, size - 2), random.randint(1, size - 2)
            while (portal_a_x == portal_b_x and portal_a_y == portal_b_y) or maze[portal_a_x][portal_a_y] != PATH or maze[portal_b_x][portal_b_y] != PATH:
                portal_a_x, portal_a_y = random.randint(1, size - 2), random.randint(1, size - 2)
                portal_b_x, portal_b_y = random.randint(1, size - 2), random.randint(1, size - 2)
            maze[portal_a_x][portal_a_y] = PORTAL
            maze[portal_b_x][portal_b_y] = PORTAL
        
    # Placement de l'étoile    
    if star_x == None and star_y == None:
        star_x, star_y = random.randint(1, size - 2), random.randint(1, size - 2)
        maze[star_x][star_y] = STAR
        

    
    # Définition de la position initiale de Thésée
    if x == None and y == None:
        x, y = entry_x, entry_y
        maze[x][y] = "\033[1;33mT\033[0m" #Thésée
    
    # Boucle de jeu
    print("\n"*24)
    if minaumort == None :
        minaumort = False
    minopamort = False
    INVINCIBLE = False
    if min_x == None and min_y == None :
        pos_min = "notOK"
    else: 
        pos_min ="OK"
    deplace_mino = False
    sauvegarder = False
    
    while maze[x][y] != EXIT:
        if level == 2 :
            if minaumort == True: # Placement de la sortie
                print("\033[1;32mFélicitations ! Vous avez atteint le Minotaure !\033[0m")
                #Placement de la sortie
                if exit_x == None and exit_y == None :
                    exit_x, exit_y = random.randint(1, size - 1), random.randint(0, size - 1)
                    maze[size - 1][random.randint(1, size - 2)] = EXIT
                    minaumort = "OK" #Pour éviter un placement infini de la sortie du au True en bas
       
        #Il faut atteindre le minautor avant que la sortie n'apparaisse
        while minaumort == False :
            print("Nombre de points restant", score)
                
            # On s'assure que le Minotaure soit bien placé  
            if deplace_mino == False :
                if pos_min == "notOK" :
                    min_x, min_y = 8,6
                    maze[min_x][min_y] = MIN
                    pos_min = "ok"
                    
                if level == 2:
                    while True:
                        maze[min_x][min_y] = PATH
                        direction_x, direction_y = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
                        next_x, next_y = min_x + direction_x, min_y + direction_y
                        if next_x < 0 or next_x >= size or next_y < 0 or next_y >= size or maze[next_y][next_x] == WALL:
                            continue
                        else:
                            break
                    
                    maze[next_x][next_y] = MIN
                    min_x, min_y = next_x, next_y
                deplace_mino = True
           

            if maze[x][y] == STAR:
                INVINCIBLE = True
                pygame.mixer.music.stop()
                pygame.mixer.init()
                pygame.mixer.music.load('Super Mario Bros - Star.mp3')
                pygame.mixer.music.play()
          
                
            if maze[x][y] == EXIT :
                print("Atteignez le Minautor avant !")
                minopamort = True
                
            if maze[x][y] == MIN :
                champi.play()
                print("\033[1;32mFélicitations ! Vous avez atteins le Minotaure !\033[0m")
                if INVINCIBLE == True :
                    INVINCIBLE = False
                    pygame.mixer.music.stop()
                    pygame.mixer.init()
                    pygame.mixer.music.load('Super-Mario-Bros.-Theme-Song.wav')
                    pygame.mixer.music.play()
                    
                minaumort = True
                
            else:
           
                # Affichage du labyrinthe avec la position de Thésée
                if INVINCIBLE == True :
                    if maze[x][y] == WALL :
                        boup.play()
                    for i, row in enumerate(maze):
                        if i == x:
                            row[y] = "\033[1;33mT\033[0m"
                        print(" ".join(row).replace(PATH, " ").replace(TRAIL, ".").replace(PORTAL, "\033[1;32mP\033[0m").replace(MIN, "\033[1;31mM\033[0m").replace(EXIT, "S"))
                else:
                    for i, row in enumerate(maze):
                        if i == x:
                            row[y] = "\033[41mT\033[0m"
                        print(" ".join(row).replace(PATH, " ").replace(TRAIL, ".").replace(PORTAL, "\033[1;32mP\033[0m").replace(MIN, "\033[1;31mM\033[0m").replace(EXIT, "S"))
            
                
                # Récupération de la saisie utilisateur
                direction = input("Où voulez-vous aller ? (z,s,q,d,a,e,w,x) : ")


            
                # Mise à jour de la position de Thésée
                if direction == "z" and x > 0 and (INVINCIBLE or maze[x - 1][y] != WALL):
                    maze[x][y] = TRAIL
                    x -= 1 if INVINCIBLE else 1
                    score -= 1 if not INVINCIBLE else 0
                    
                    

                    if minopamort == True : #Réapparition de la sortie
                        maze[x+1][y] = EXIT
                        minopamort = False
                        
                elif direction == "s" and x < size - 1 and (INVINCIBLE or maze[x + 1][y] != WALL):
                    maze[x][y] = TRAIL
                    x += 1 if INVINCIBLE else 1
                    score -= 1 if not INVINCIBLE else 0
                    
                    if minopamort == True :
                        maze[x-1][y] = EXIT
                        minopamort = False
                    
                elif direction == "q" and y > 0 and (INVINCIBLE or maze[x][y - 1] != WALL):
                    maze[x][y] = TRAIL
                    y -= 1 if INVINCIBLE else 1
                    score -= 1 if not INVINCIBLE else 0
                    
                    if minopamort == True :
                        maze[x][y+1] = EXIT
                        minopamort = False
                        
                elif direction == "d" and y < size - 1 and (INVINCIBLE or maze[x][y + 1] != WALL):
                    maze[x][y] = TRAIL
                    y += 1 if INVINCIBLE else 1
                    score -= 1 if not INVINCIBLE else 0
                    
                    if minopamort == True :
                        maze[x][y-1] = EXIT
                        minopamort = False
                    
                elif direction == "a" and y < size - 1 and (INVINCIBLE or maze[x-1][y-1] != WALL):
                    maze[x][y] = TRAIL
                    x -= 1 if INVINCIBLE else 1
                    y -= 1 if INVINCIBLE else 1
                    score -= 1 if not INVINCIBLE else 0
                    
                    if minopamort == True :
                        maze[x+1][y+1] = EXIT
                        minopamort = False
                        
                elif direction == "e" and y < size - 1 and (INVINCIBLE or maze[x-1][y + 1] != WALL):
                    maze[x][y] = TRAIL
                    x -= 1 if INVINCIBLE else 1
                    y += 1 if INVINCIBLE else 1
                    score -= 1 if not INVINCIBLE else 0
                    
                    if minopamort == True :
                        maze[x+1][y-1] = EXIT
                        minopamort = False
                        
                elif direction == "w" and y < size - 1 and (INVINCIBLE or maze[x+1][y-1] != WALL):
                    maze[x][y] = TRAIL
                    x += 1 if INVINCIBLE else 1
                    y -= 1 if INVINCIBLE else 1
                    score -= 1 if not INVINCIBLE else 0
                    
                    if minopamort == True :
                        maze[x-1][y+1] = EXIT
                        minopamort = False
                        
                elif direction == "x" and y < size - 1 and (INVINCIBLE or maze[x+1][y + 1] != WALL):
                    maze[x][y] = TRAIL
                    x += 1 if INVINCIBLE else 1
                    y += 1 if INVINCIBLE else 1
                    score -= 1 if not INVINCIBLE else 0
                        
                    if minopamort == True :
                        maze[x-1][y-1] = EXIT
                        minopamort = False
                        
                elif direction == "stop" :
                    pygame.mixer.music.stop()
                    break
                
                elif direction == "quit" :
                    sauvegarder = True
                    break
                
                
                
                        
                print("\n"*24)


                # Vérification si Thésée est sur un portail
                if maze[x][y] == PORTAL:
                    # Trouver l'autre portail correspondant
                    portal_a_x, portal_a_y = -1, -1
                    portal_b_x, portal_b_y = -1, -1
                    for i in range(size):
                        for j in range(size):
                            if maze[i][j] == PORTAL and (i != x or j != y):
                                if portal_a_x == -1:
                                    portal_a_x, portal_a_y = i, j
                                else:
                                    portal_b_x, portal_b_y = i, j
                                    break
                        if portal_b_x != -1:
                            break
            
                    # Téléportation de Thésée
                    if x == portal_a_x and y == portal_a_y:
                        x, y = portal_b_x, portal_b_y
                    else:
                        x, y = portal_a_x, portal_a_y
                        pipe.play(1)
                
                if score <= 0 :
                    break
            
            deplace_mino = False
            if sauvegarder == True :
                break
            
            
        maze[star_x][star_y] = PATH       
      ######## FIN WHILE #############
      ######## SECOND WHILE ##########
        if sauvegarder == True :
                break  
        print("Nombre de points restant", score)
        if score <= 0 :
            break
        if maze[x][y] == STAR:
            INVINCIBLE = True
            pygame.mixer.music.stop()
            pygame.mixer.init()
            pygame.mixer.music.load('Super Mario Bros - Star.mp3')
            pygame.mixer.music.play()
            t.sleep(3)
            pygame.mixer.music.stop()
            INVINCIBLE = False



                
     # Affichage du labyrinthe avec la position de Thésée
        for i, row in enumerate(maze):
            if i == x:
                row[y] = "\033[41mT\033[0m"
            print(" ".join(row).replace(PATH, " ").replace(TRAIL, ".").replace(PORTAL, "\033[1;32mP\033[0m").replace(MIN, "\033[1;31mM\033[0m").replace(EXIT, "S"))
    
    
    
        
    # Récupération de la saisie utilisateur
        direction = input("Où voulez-vous aller ? (z,s,q,d,a,e,w,x) : ")
            
        # Mise à jour de la position de Thésée
        if direction == "z" and x > 0 and (INVINCIBLE or maze[x - 1][y] != WALL):
                    maze[x][y] = TRAIL
                    x -= 1 if INVINCIBLE else 1
                    score -= 1 if not INVINCIBLE else 0
                
        elif direction == "s" and x < size - 1 and (INVINCIBLE or maze[x + 1][y] != WALL):
                    maze[x][y] = TRAIL
                    x += 1 if INVINCIBLE else 1
                    score -= 1 if not INVINCIBLE else 0
            
        elif direction == "q" and y > 0 and (INVINCIBLE or maze[x][y - 1] != WALL):
                    maze[x][y] = TRAIL
                    y -= 1 if INVINCIBLE else 1
                    score -= 1 if not INVINCIBLE else 0
                
        elif direction == "d" and y < size - 1 and (INVINCIBLE or maze[x][y + 1] != WALL):
                    maze[x][y] = TRAIL
                    y += 1 if INVINCIBLE else 1
                    score -= 1 if not INVINCIBLE else 0
            
        elif direction == "a" and y < size - 1 and (INVINCIBLE or maze[x-1][y-1] != WALL):
                    maze[x][y] = TRAIL
                    x -= 1 if INVINCIBLE else 1
                    y -= 1 if INVINCIBLE else 1
                    score -= 1 if not INVINCIBLE else 0
                
        elif direction == "e" and y < size - 1 and (INVINCIBLE or maze[x-1][y + 1] != WALL):
                    maze[x][y] = TRAIL
                    x -= 1 if INVINCIBLE else 1
                    y += 1 if INVINCIBLE else 1
                    score -= 1 if not INVINCIBLE else 0
                
        elif direction == "w" and y < size - 1 and (INVINCIBLE or maze[x+1][y-1] != WALL):
                    maze[x][y] = TRAIL
                    x += 1 if INVINCIBLE else 1
                    y -= 1 if INVINCIBLE else 1
                    score -= 1 if not INVINCIBLE else 0
                
        elif direction == "x" and y < size - 1 and (INVINCIBLE or maze[x+1][y + 1] != WALL):
                    maze[x][y] = TRAIL
                    x += 1 if INVINCIBLE else 1
                    y += 1 if INVINCIBLE else 1
                    score -= 1 if not INVINCIBLE else 0
                
        elif direction == "stop" :
            pygame.mixer.music.stop()
            break
        
        elif direction == "quit" :
            sauvegarder = True

        print("\n"*24)
        # Vérification si Thésée est sur un portail
        if maze[x][y] == PORTAL:
            # Trouver l'autre portail correspondant
            portal_a_x, portal_a_y = -1, -1
            portal_b_x, portal_b_y = -1, -1
            for i in range(size):
                for j in range(size):
                    if maze[i][j] == PORTAL and (i != x or j != y):
                        if portal_a_x == -1:
                            portal_a_x, portal_a_y = i, j
                        else:
                            portal_b_x, portal_b_y = i, j
                            break
                if portal_b_x != -1:
                    break
    
            # Téléportation de Thésée
            if x == portal_a_x and y == portal_a_y:
                x, y = portal_b_x, portal_b_y
            else:
                x, y = portal_a_x, portal_a_y
                pipe.play(1)
        

    sauvegarder_jeu(maze, entry_x, entry_y, x, y, exit_x, exit_y, min_x, min_y, star_x, star_y, portal_a_x, portal_a_y, portal_b_x, portal_b_y, level, score, minaumort)
    temps2 = t.time()
    temps = temps2 - temps1
    
    if sauvegarder == True :
        print("\033[1;32mRevenez quand vous voulez !\033[0m")
        print("Voici votre temps actuel : ", round(temps), "secondes")
        print("Voici votre score actuel : ", score, "points")
        
    else:
        if score <= 0 :       
            print("\033[1;31mG A M E  O V E R\033[0m")
            pygame.mixer.music.stop()
            pygame.mixer.init()
            pygame.mixer.music.load('Mario Death - Sound Effect (HD).mp3')
            pygame.mixer.music.play()
        
        if score> 1 :
            pygame.mixer.music.stop()
            pygame.mixer.init()
            pygame.mixer.music.load('Super Mario Bros. - Course Clear Sound Effect.mp3')
            pygame.mixer.music.play()
            print("\033[1;32mFéliciation, vous avez gagné !\033[0m")
        print("Voici votre temps : ", round(temps), "secondes")
        print("Voici votre score : ", score, "points")

while True : 
    Laby()
    R = Rejouer()
    if not R:
        break
    
    
# Charger le jeu sauvegardé
def charger_jeu():
    try:
        with open("sauvegarde_jeu.pickle", "rb") as fichier:
            etat_jeu = pickle.load(fichier)
            return Laby(etat_jeu["maze"], etat_jeu["entry_x"], etat_jeu["entry_y"], etat_jeu["x"], etat_jeu["y"], etat_jeu["exit_x"], etat_jeu["exit_y"], etat_jeu["min_x"], etat_jeu["min_y"], etat_jeu["star_x"], etat_jeu["star_y"], etat_jeu["portal_a_x"], etat_jeu["portal_a_y"], etat_jeu["portal_b_x"], etat_jeu["portal_b_y"], etat_jeu["level"], etat_jeu["score"], etat_jeu["minaumort"])
    except FileNotFoundError:
        return None
    
    # Charger le jeu sauvegardé
    etat_jeu_charge = charger_jeu()
    if etat_jeu_charge:
        maze, entry_x, entry_y, x, y, exit_x, exit_y, min_x, min_y, star_x, star_y, portal_a_x, portal_b_x, portal_b_x, portal_b_y, level, score, minaumort = etat_jeu_charge
        # Continuer la partie à partir de l'état chargé
    else:
        # Aucune sauvegarde trouvée, commencer une nouvelle partie 
        Laby()   
    
    
'''

    Sortie soit en bas, soit à droite qui marche pas :
        
        exit_x, exit_y = random.randint(1, size - 2), random.randint(1, size - 2)
                        if random.choice([True, False]):
                            exit_x = size - 1
                            maze[exit_y][exit_x] = EXIT
                            minaumort = "OK" #Pour éviter un placement infini de la sortie du au True
    '''