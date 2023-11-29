import pygame
import random
enemy_maxspeed = 2
enemy_minspeed = 1

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load('../Final Project/photo/enemycar.png').convert()
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(enemy_minspeed, enemy_maxspeed)

enemies = pygame.sprite.Group()