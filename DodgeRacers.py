import time

import pygame
import random
#from player import Player


pygame.init()

#create the window
screen_width = 500
screen_height = 500
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Dodge Racers")

#colors
gray = (100, 100, 100)
green = (76, 208, 56)
red = (200, 0, 0)
white = (255, 255, 255)
yellow = (255, 232, 0)

# game settings
speed = 2
score = 0

# road, edge markers, lanes
road = (100, 0, 300, screen_height)

marker_width = 10
marker_height = 50
left_edge_marker = (95, 0, marker_width, screen_height)
right_edge_marker = (395, 0, marker_width, screen_height)

left_lane = 150
center_lane = 250
right_lane = 350
lanes = [left_lane, center_lane, right_lane]

#movement of the lane markers
lane_marker_move_y=0





def draw_welcome(screen):
    Title_font = pygame.font.Font('../Final Project/photo/score_font/custom_font.ttf', 64)

    Start_font = pygame.font.Font('../Final Project/photo/score_font/custom_font.ttf', 60)
    Title = Title_font.render("Dodge Racers", True, (155, 155, 255))
    start = Start_font.render("Press enter to start", True, (155, 155, 255))
    screen.blit(Title, (screen_width/2 - Title.get_width()/2 , screen_height/2 - Title.get_height()/2))
    screen.blit(start, (screen_width/1.5 - start.get_width()/1.5, screen_height/1.5 - start.get_height()/1.5))
draw_mess = True


if draw_mess:
    screen.blit(screen,(0,0))
    draw_welcome(screen)
    pygame.display.flip()
    time.sleep(4)

class Vehicle(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        image_scale = 85 / image.get_rect().width
        new_width = image.get_rect().width * image_scale
        new_height = image.get_rect().height * image_scale
        self.image = pygame.transform.scale(image, (new_width, new_height))

        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
class PlayerVehicle(Vehicle):
    def __init__(self, x, y):
        image = pygame.image.load('../Final Project/photo/playercar.png')
        super().__init__(image, x, y)
player_x = 250
player_y = 400

player_group = pygame.sprite.Group()
player = PlayerVehicle(player_x, player_y)
player_group.add(player)

#load the other vehicles
image_filenames = ['enemycar.png', 'enemycar2.png', 'enemycar3.png', 'oil.png']
enemy_images = []
for image_filename in image_filenames:
    image = pygame.image.load('photo/' + image_filename)
    enemy_images.append(image) #17:58

#loop for game
clock = pygame.time.Clock()
fps = 120
running = True
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and player.rect.center[0] > left_lane:
                player.rect.x -= 100
            elif event.key == pygame.K_RIGHT and player.rect.center[0] < right_lane:
                player.rect.x += 100
        # if game_state == "start_menu":
        #     draw_start_menu()
        # if game_state == "game":
        #     keys= pygame.key.get_pressed()
        # if game_state == "start_menu":
        #     keys= pygame.key.get_pressed()
        #     if keys[pygame.K_SPACE]:
        #         game_state = 'game'
    #draw the grass
    screen.fill(green)

    # draw the road and markers
    pygame.draw.rect(screen, gray, road) #creats the road
    pygame.draw.rect(screen, yellow, left_edge_marker)
    pygame.draw.rect(screen, yellow, right_edge_marker)


    #draw the lane markers
    lane_marker_move_y += speed * 2
    if lane_marker_move_y >= marker_height * 2:
        lane_marker_move_y = 0 # in this case, the lane markers are whats moving in order to give the image of a moving road
    for y in range(marker_height * -2, screen_height, marker_height * 2):
        pygame.draw.rect(screen, white, (left_lane +45, y + lane_marker_move_y, marker_width, marker_height))
        pygame.draw.rect(screen, white, (center_lane + 45, y + lane_marker_move_y, marker_width, marker_height))

    #draw the player's car
    player_group.draw(screen)
    # what makes the player's car move
    # if event.type == pygame.KEYDOWN:
    #     if event.key == pygame.K_LEFT:
    #         player.move_left()
    #     if event.key == pygame.K_RIGHT:
    #         player.move_right()
    # player.update()
    # player.draw(screen)

    pygame.display.update()


pygame.quit
