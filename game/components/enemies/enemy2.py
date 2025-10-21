import pygame
import random 
from pygame.sprite import Sprite
from game.utils.constants import ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH
from game.components.bullets.bullet import Bullet

class Enemy2(Sprite):
    X_POS_LIST = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    Y_POS = 20
    SPEED_Y = 1
    SPEED_X = 10
    MOV_X = {0: "left", 1: "right"}
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    
    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.SHIP_WIDTH, self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS_LIST[random.randint(0, 9)]
        self.rect.y = self.Y_POS 
        self.speed_y = self.SPEED_Y
        self.speed_x = self.SPEED_X
        self.movement_x =  self.MOV_X[random.randint(0, 1)]
        self.index = 0
        self.move_x_for = random.randint(30, 100)
        self.move_distance = random.randint(150, 300)
        self.move_direction = 1
        self.move_counter = 0
        self.random_move_chance = 0.2
        self.type = 'enemy'
        self.shooting_time = random.randint(30,50)
        
    def update(self, ships, game):
        self.rect.y += self.speed_y
        self.shoot(game.bullet_manager)
        
        #Mover name enemiga de izquierda a derecha, pero cuando llega al limite del movimiento hay una chance de que no regrese y siga por otro ciclo en la misma direccion
        if random.random() < self.random_move_chance:    # genera un numero aleatorio entre 0.0 y 1.0, y lo compara con la variable self.random_move_chance
            self.move_direction *= -1  # Cambiar de dirección
            
        if self.move_counter < self.move_distance:
            self.rect.x += self.speed_x * self.move_direction
            self.move_counter += abs(self.speed_x)
        else:
            self.move_counter = 0
            self.move_direction *= -1  # Cambiar la dirección del movimiento zigzag

        # Cambiar la dirección de movimiento horizontal cuando se alcanzan los bordes
        if self.rect.x <= 0 or self.rect.x >= SCREEN_WIDTH - self.SHIP_WIDTH:
            self.speed_x = -self.speed_x
            
        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)
            
    def draw(self, screen):
            screen.blit(self.image, (self.rect.x, self.rect.y))
            
    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        # if shooting time is lees than current time, create a new bullet
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(30, 50)
            
    #def change_movement_x(self):
     #   self.index += 1
      #  
        #validate if ship moves to left position or right position
       # if (self.index >= self.move_x_for and self.movement_x == "right") or (self.rect.x >= SCREEN_WIDTH - self.SHIP_WIDTH // 2):
        #    self.movement_x = "left"
         #   self.index = 0
        #elif (self.index >= self.move_x_for and self.movement_x == "left") or (self.rect.x <= self.SHIP_WIDTH // 2):
           # self.movement_x = "right"
           # self.index = 0
    