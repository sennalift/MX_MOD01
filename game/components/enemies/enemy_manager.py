import random  #se importa el modulo random
from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy2 import Enemy2  # se importa la clase Enemy2
from game.components.enemies.enemy3 import Enemy3  # se importa la clase Enemy3

class EnemyManager():
    def __init__(self):
        self.enemies = []

    def update(self, game):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies, game)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        enemy_type = random.randint(1, 3)
        
        if enemy_type == 1:
            enemy = Enemy()
            
        elif enemy_type == 2:
            x_speed = 5
            y_speed = 2
            move_x_for = random.choice([50, 120])
            enemy = Enemy(enemy_type, x_speed, y_speed, move_x_for)
        
        elif enemy_type == 3:
            x_speed = 7
            enemy = Enemy(enemy_type, x_speed)

        if len(self.enemies) < 1:
            self.enemies.append(enemy)