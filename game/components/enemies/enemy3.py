import pygame
import random 
from pygame.sprite import Sprite
from game.utils.constants import ENEMY_3, SCREEN_WIDTH
from game.components.bullets.bullet import Bullet

class Enemy3(Sprite):
    SPEED_X = 10
    MOV_X = {0: "left", 1: "right"}
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    
    def __init__(self):
        self.image = ENEMY_3  # Carga la imagen de la nave enemiga
        self.image = pygame.transform.scale(self.image, (self.SHIP_WIDTH, self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.type = 'enemy'
        self.shooting_time = random.randint(30,50)
        
        self.generate_initial_position()

    def generate_initial_position(self):
        self.spawn_side = random.choice(["left", "right"])  # esta funcion elige donde debe de aparecer la nave de manera aleatoria.
        
        if self.spawn_side == "left":
            self.rect.x = 0
            self.speed_x = self.SPEED_X  # Velocidad hacia la derecha
        else:
            self.rect.x = SCREEN_WIDTH - self.SHIP_WIDTH
            self.speed_x = -self.SPEED_X  # Velocidad hacia la izquierda
        
        self.rect.y = self.generate_random_y()

    def generate_random_y(self):
        # Establecer límites para la generación de coordenadas Y
        min_y = 50  # Coordenada Y mínima
        max_y = 200  # Coordenada Y máxima
        return random.randint(min_y, max_y)
        
    def update(self, ships, game):
        self.rect.x += self.speed_x
        self.shoot(game.bullet_manager)
        
        # Comprobar si la nave ha llegado al borde opuesto
        if (self.spawn_side == "left" and self.rect.x >= SCREEN_WIDTH) or \
           (self.spawn_side == "right" and self.rect.x <= -self.SHIP_WIDTH):
            ships.remove(self)  # Eliminar la nave cuando llega al borde opuesto

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        # if shooting time is lees than current time, create a new bullet
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(30, 50)