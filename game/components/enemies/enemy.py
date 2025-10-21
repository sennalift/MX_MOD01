
import pygame
import random 
from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1, ENEMY_2, ENEMY_3, SCREEN_HEIGHT, SCREEN_WIDTH
from game.components.bullets.bullet import Bullet

class Enemy(Sprite):
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
    Y_POS = 20
    SPEED_Y = 1
    SPEED_X = 5
    MOV_X = {0: "left", 1: "right"}
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    
    def __init__(self, enemy_type=None, x_speed=None, y_speed=None, move_x_for=None):
        super().__init__()

        self.image = ENEMY_1
        self.image = pygame.transform.scale(self.image, (self.SHIP_WIDTH, self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS_LIST[random.randint(0, 19)]
        self.rect.y = self.Y_POS
        self.speed_y = self.SPEED_Y
        self.speed_x = self.SPEED_X
        self.movement_x = self.MOV_X[random.randint(0, 1)]
        self.index = 0
        self.move_x_for = self.MOV_X[0]
        self.type = 'enemy'
        self.shooting_time = random.randint(30, 50)
        
        if enemy_type == 2:
            self.image = ENEMY_2
            self.image = pygame.transform.scale(self.image, (self.SHIP_WIDTH, self.SHIP_HEIGHT))
            self.speed_x = x_speed if x_speed is not None else self.speed_x
            self.speed_y = y_speed if y_speed is not None else self.speed_y
            self.move_x_for = move_x_for if move_x_for is not None else self.move_x_for
            self.shooting_time = random.randint(30, 50)
        elif enemy_type == 3:
            self.image = ENEMY_3
            self.image = pygame.transform.scale(self.image, (self.SHIP_WIDTH, self.SHIP_HEIGHT))
            self.speed_x = x_speed if x_speed is not None else self.speed_x
            self.shooting_time = random.randint(30, 50)
            # ... (other attributes specific to Enemy3)

    def update(self, ships, game):
        self.rect.y += self.speed_y
        # shoot a bullet
        self.shoot(game.bullet_manager)
        # Move enemy to left or right position
        if self.movement_x == "left":
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x
            
        self.change_movement_x()
            
        # Remove ship when it is outside of the screen
        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def change_movement_x(self):
        self.index += 1
        # Validate if ship moves to left or right position
        if (self.index >= self.move_x_for and self.movement_x == "right") or (self.rect.x >= SCREEN_WIDTH - self.SHIP_WIDTH // 2):
            self.movement_x = "left"
            self.index = 0
        elif (self.index >= self.move_x_for and self.movement_x == "left") or (self.rect.x <= self.SHIP_WIDTH // 2):
            self.movement_x = "right"
            self.index = 0
            
    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        # If shooting time is less than current time, create a new bullet
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(30, 50)