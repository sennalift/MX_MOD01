
import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT

class Spaceship(Sprite):
    X_POS =(SCREEN_WIDTH // 2) - 40 
    Y_POS = 500
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS 
        self.rect.y = self.Y_POS
        self.type = 'player'
    
    def update(self, user_input):
        if user_input[pygame.K_a]:
            self.move_left()
            
        elif user_input[pygame.K_d]:
            self.move_right()
            
        elif user_input[pygame.K_w]:
            self.move_up()
            
        elif user_input[pygame.K_s]:
            self.move_down()
        
        elif user_input[pygame.K_q]:
            self.move_left_up()
            
        elif user_input[pygame.K_e]:
            self.move_right_up()
            
        elif user_input[pygame.K_z]:
            self.move_left_down
            
        elif user_input[pygame.K_x]:
            self.move_right_down
        
    
    def move_left(self):  #implemente la solucion que dio el trainer en la clase, ya que la solucion que yo implemente, aunque funcionaba tenia un pequeño error
        self.rect.x -= 10
        if self.rect.right <= 0: 
            self.rect.x = SCREEN_WIDTH -40 
              
    
    def move_right(self):  #implemente la solucion que dio el trainer en la clase, ya que la solucion que yo implemente, aunque funcionaba tenia un pequeño error
        self.rect.x += 10
        if self.rect.left >= SCREEN_WIDTH:  
            self.rect.x = 0  
    
    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= 10
            
    
    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y += 10 
    
    def move_left_up(self):  #comportamiento de movimiento en diagonal izquierda arriba
        self.rect.y -= 10 #up
        self.rect.x -= 10 #left
        if self.rect.right <= 0: 
            self.rect.x = SCREEN_WIDTH -40
    
    def move_right_up(self): #comportamiento de movimiento en diagonal derecha arriba
        self.rect.y -= 10 #up
        self.rect.x += 10 #right
        if self.rect.left >= SCREEN_WIDTH:  
            self.rect.x = 0 
        
    def move_left_down(self):
        pass
        
    def move_right_down(self):
        pass
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
