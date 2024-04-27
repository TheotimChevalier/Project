'''
Created on 23 avr. 2023

@author: Me
'''
'''
Created on 15 avr. 2023

@author: Me
'''
'''
Created on 15 avr. 2023

@author: Me
'''

import pygame
import time
import random
from typing import List

WINDOW_X = 400
WINDOW_Y = 300

# Vitesse du serpent
SNAKE_SPEED = 10

# Définition des couleurs
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GREEN = pygame.Color(0, 255, 0)
RED = pygame.Color(255, 0, 0)

class Case:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        
    def __repr__(self):
        return f'Case({self.x}, {self.y})'
        
    def __str__(self):
        return f'({self.x}, {self.y})'


class Snake:
    def __init__(self, cases: List[Case]):
        self.cases = cases
        self.direction = "RIGHT"
        
    def head(self) -> Case:
        return self.cases[0]
        
    def get_all_cases(self) -> List[Case]:
        return self.cases
        
        
    def get_new_case(self) -> Case:
        """
        Return the new case that will be added to the snake's head, based on the current direction.
        """
        x, y = self.head().x, self.head().y
        if self.direction == "UP":
            y -= 10 
        elif self.direction == "DOWN":
            y += 10
        elif self.direction == "LEFT":
            x -= 10
        else :
            x += 10
        return Case(x, y)
        
    def move(self, new_case: Case, remove_tail: bool):
        if new_case is not None:
            self.cases.insert(0, new_case)
        if remove_tail:
            self.cases.pop()
        
    def is_out_of_frame(self) -> bool:
        x, y = self.head().x, self.head().y
        return x < 0 or y < 0 or x >= WINDOW_X-10 or y >= WINDOW_Y-10
        
    def is_head_touching_body(self) -> bool:
        for c in self.cases[1:]:
            if c == self.head():
                return True
        return False
    
    def grow(self):
        self.cases.append(self.cases[-1])
        
    def change_direction(self, direction):
        self.direction = direction


def new_fruit(snake):
    """
    Generate a new fruit at a random position that is not occupied by the snake.
    """
    while True:
        x = random.randrange(10, WINDOW_X - 10, 10)
        y = random.randrange(10, WINDOW_Y - 10, 10)
        fruit = Case(x, y)
        for case in snake.get_all_cases():
            if case == fruit:
                break
        else:
            return fruit


def game_over(score):
    """
    Display Game Over message and score, and wait for 2 seconds before quitting the game.
    """
    game_window.fill(BLACK)
    surface = pygame.font.SysFont('times new roman', 40).render('Game Over', True, RED)
    rect = surface.get_rect()
    rect.center = (WINDOW_X // 2, WINDOW_Y // 2 - 30)
    
    game_window.blit(surface, rect)
    surface = pygame.font.SysFont('times new roman', 20).render('Score : ' + str(score), True, WHITE)
    rect = surface.get_rect()
    rect.center = (WINDOW_X // 2, WINDOW_Y // 2 + 10)
    game_window.blit(surface, (0, 0))
    


pygame.init()

# Initialisation de la fenêtre de jeu
pygame.display.set_caption('Jeu du serpent')
game_window = pygame.display.set_mode((WINDOW_X, WINDOW_Y))

# Contrôleur de FPS (images par seconde)
fps = pygame.time.Clock()

# Position initiale du serpent et direction
snake = Snake([Case(50, 50), Case(40, 50), Case(30, 50)])

# Position initiale du fruit
fruit = new_fruit(snake)

# Score initial
score = 0

# Fonction principale
while True:

    # Gestion des événements clavier
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction("UP")
            if event.key == pygame.K_DOWN:
                snake.change_direction("DOWN")
            if event.key == pygame.K_LEFT:
                snake.change_direction("LEFT")
            if event.key == pygame.K_RIGHT:
                snake.change_direction("RIGHT")
                
    def draw_snake(snake):
        """
        Draw the snake on the game window.
        """
        for case in snake.get_all_cases():
            pygame.draw.rect(game_window, GREEN, (case.x, case.y, 10, 10))
            
    def draw_fruit(fruit):
        """
        Draw the fruit on the game window.
        """
        pygame.draw.rect(game_window, RED, (fruit.x, fruit.y, 10, 10))     
        
    # Calcul de la nouvelle position du snake
    new_case = snake.get_new_case() 
    
    # Si la nouvelle position du snake correspond à la position de la pomme, le snake mange la pomme
    if new_case == fruit:
        fruit = new_fruit(snake)
        score += 1
        snake.grow()
        if SNAKE_SPEED < 25:
            SNAKE_SPEED += 1
            
    # Si le serpent sort de l'écran ou touche son corps, le jeu est terminé
    if snake.is_out_of_frame() or snake.is_head_touching_body():
        game_over(score)
        pygame.display.update()
        time.sleep(5)
        pygame.quit()
        quit()
        
    # Afficher le score
    surface = pygame.font.SysFont('times new roman', 20).render('Score : ' + str(score), True, WHITE)
    rect = surface.get_rect()
    game_window.blit(surface, rect)    
    
    # Déplacement du snake
    snake.move(new_case, remove_tail=True)
    

    # Dessin de la scène
    game_window.fill(BLACK)
    draw_snake(snake)
    draw_fruit(fruit)
    pygame.display.update()
    fps.tick(SNAKE_SPEED)
pygame.quit()
quit()
