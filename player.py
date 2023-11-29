import pygame
player_speed = 2


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.forward_image = pygame.image.load("../Final Project/photo/playercar.png").convert()
        self.forward_image.set_colorkey((255,255,255))
        self.reverse_image = pygame.transform.flip(self.forward_image, True, False)
        self.image = self.forward_image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x,y)
        self.x_velocity = 0
        self.y_velocity = 0
    def move_up(self):
        self.y_velocity = -player_speed
    def move_down(self):
        self.y_velocity = player_speed
    def move_left(self):
        self.x_velocity = -1 * player_speed
        self.image = self.reverse_image
    def move_right(self):
        self.x_velocity = player_speed
        self.image = self.forward_image
    def stop(self):
        self.y_velocity = 0
        self.x_velocity = 0
    def update(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
        self.rect.x = self.x
        self.rect.y = self.y
    def draw(self, screen):
        screen.blit(self.image, self.rect)
