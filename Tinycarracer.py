
import pygame
import random
import math



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
power_up_timer = 0

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

#audio for when the car crashes into an enemy
pygame.mixer.init()
car_crash = pygame.mixer.Sound('../carmen_final_game_project/photo/car_crash.mp3')

#functions to save high scores
def load_high_score():
    try:
        with open("high_score.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0
def save_high_scores(score):
    with open("high_score.txt", "w") as file:
        file.write(str(score))
high_score = load_high_score()

#class for the vehicles to fit in the lanes
class Vehicle(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        image_scale = 85 / image.get_rect().width
        new_width = image.get_rect().width * image_scale
        new_height = image.get_rect().height * image_scale
        self.image = pygame.transform.scale(image, (new_width, new_height))

        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

#An extension of the Vehicle class to fit specifically for the player
class PlayerVehicle(Vehicle):
    def __init__(self, x, y):
        image = pygame.image.load('../carmen_final_game_project/photo/playercar.png')
        super().__init__(image, x, y)

#another extension of the Vehicle class for the power up
class PowerUp(Vehicle):
    def __init__(self, x, y):
        image = pygame.image.load('photo/powerup.png')
        super().__init__(image, x, y)
    def draw(self, screen):
        screen.blit(self.image, self.rect)
power_up_group = pygame.sprite.Group()

#creating the bullets
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, target_x, target_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill((255, 0, 0))  # Red color for the bullet
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10
        angle = math.atan2(target_y - y, target_x -x)
        self.velocity = [5* math.cos(angle), 5 *math.sin(angle)]
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if self.rect.bottom < 0 or self.rect.top > screen_height or self.rect.right < 0 or self.rect.left > screen_width:
            self.kill()
def create_bullet(target_x, target_y):
    bullet = Bullet(player.rect.center[0], player.rect.top, event.pos[0], event.pos[1])
    bullet_group.add(bullet)
bullet_group = pygame.sprite.Group()

#determining the player's start position in the game
player_x = 250
player_y = 400

player_group = pygame.sprite.Group()
player = PlayerVehicle(player_x, player_y)
player_group.add(player)

#code for the looping background music
pygame.mixer_music.load('backgroundmusic.mp3')
pygame.mixer_music.play(-1)



#load the other vehicles
image_filenames = ['enemycar.png', 'enemycar2.png', 'enemycar3.png', 'oil.png']
vehicle_images = []
for image_filename in image_filenames:
    image = pygame.image.load('photo/' + image_filename)
    vehicle_images.append(image)

#sprite group for enemy vehicles
vehicle_group = pygame.sprite.Group()

crash = pygame.image.load('photo/crash.png')
crash_rect = crash.get_rect()

#the function to create the main menu
def draw_menu(screen): #courtney mccloughan helped me with this
    screen.fill(green)
    pygame.draw.rect(screen, gray, road)  # creats the road
    pygame.draw.rect(screen, yellow, left_edge_marker)
    pygame.draw.rect(screen, yellow, right_edge_marker)
    menu_font = pygame.font.Font("../carmen_final_game_project/photo/score_font/Blazed.ttf", 50)
    menu_text = menu_font.render("Dodge Racers", True, (255,100,10))
    menu_text_rect = menu_text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
    press_enter_font = pygame.font.Font("../carmen_final_game_project/photo/score_font/Amatic-Bold.ttf", 35)
    press_enter_text = press_enter_font.render("Press Enter to Start", True, (0,0,0))
    press_enter_rect = press_enter_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
    instruction_font = pygame.font.Font("../carmen_final_game_project/photo/score_font/Amatic-Bold.ttf", 30)
    instruction_text = instruction_font.render("Use the left and right arrows to avoid the cars.", True, (0,0,0))
    instruction_text_rect = instruction_text.get_rect(center = (screen_width //2, screen_height //2 + 100))
    instruction_text2 = instruction_font.render("Collect gas cans for +2 points!", True, (0,0,0))
    instruction_text2_rect = instruction_text2.get_rect(center = (screen_width //2, screen_height//2 + 130))
    instruction_text3 = instruction_font.render("If you shoot a car, you don't get points!", True, (0, 0, 0))
    instruction_text3_rect = instruction_text2.get_rect(center=(screen_width //2, screen_height //2 + 160)) ################
    screen.blit(menu_text, menu_text_rect)
    screen.blit(press_enter_text, press_enter_rect)
    screen.blit(instruction_text, instruction_text_rect)
    screen.blit(instruction_text2, instruction_text2_rect)
    screen.blit(instruction_text3, instruction_text3_rect)
show_menu = True

while show_menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            show_menu = False
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            show_menu = False
    draw_menu(screen)
    pygame.display.flip()

gameover = False
#loop for game
clock = pygame.time.Clock()
fps = 120
running = True
Enter = True
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not gameover:
                create_bullet(event.pos[0], event.pos[1])
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.rect.center[0] > left_lane:
            player.rect.x -= 100
        elif keys[pygame.K_RIGHT] and player.rect.center[0] < right_lane:
            player.rect.x += 100
        for vehicle in vehicle_group:
            if pygame.sprite.collide_rect(player, vehicle):
                gameover = True
                car_crash.play()
                if keys[pygame.K_LEFT]:
                    player.rect.left = vehicle.rect.right
                    crash_rect.center = [player.rect.left, (player.rect.center[1] + vehicle.rect.center[1]) / 2]
                elif keys[pygame.K_RIGHT]:
                    player.rect.right = vehicle.rect.left
                    crash_rect.center = [player.rect.left, (player.rect.center[1] + vehicle.rect.center[1]) / 2]

    bullet_group.update()

    for bullet in bullet_group:
        if pygame.sprite.spritecollide(bullet, vehicle_group, True):
            bullet.kill()



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
    bullet_group.draw(screen)
    #add up to two enemies
    if len(vehicle_group) < 2:
        add_vehicle = True
        for vehicle in vehicle_group:
            if vehicle.rect.top < vehicle.rect.height * 1.5:
                add_vehicle = False
        if add_vehicle:
            lane = random.choice(lanes)
            vehicle = Vehicle(image, lane, screen_height / -2)
            image = random.choice(vehicle_images)
            vehicle_group.add(vehicle)

    for vehicle in vehicle_group:
        vehicle.rect.y +=speed
        if vehicle.rect.top >= screen_height:
            vehicle.kill()
            score += 1
            if score > 0 and score %5 == 0:
                speed +=0.5
    vehicle_group.draw(screen)
    power_up_timer += 1
    if power_up_timer % 250 == 0:
        lane= random.choice(lanes)
        power_up = PowerUp(lane, screen_height/-2)
        power_up_group.add(power_up)
    for power_up in power_up_group:
        power_up.rect.y += speed
        if pygame.sprite.collide_rect(player, power_up):
            power_up.kill()
            score+= 2
        power_up_group.draw(screen)
    font = pygame.font.Font("../carmen_final_game_project/photo/score_font/Blazed.ttf", 20)
    score_text = font.render('Score:' + str(score), True, (0, 0, 0))
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (50, 450)
    screen.blit(score_text, score_text_rect)



    #head on collision
    if pygame.sprite.spritecollide(player, vehicle_group, True):
        gameover= True
        car_crash.play()
        crash_rect.center = [player.rect.center[0], player.rect.top]
    if gameover:
        screen.blit(crash, crash_rect)
        pygame.draw.rect(screen, red, (0,50, screen_width ,100))
        font = pygame.font.Font("../carmen_final_game_project/photo/score_font/Amatic-Bold.ttf", 30)
        text = font.render("CRASH! Game over. Click anywhere to restart", True, white)
        text_rect = text.get_rect()
        text_rect.center = (screen_width / 2 , 95)
        screen.blit(text, text_rect)
        if score > high_score:
            high_score = score
            save_high_scores(high_score)
        high_score_font = pygame.font.Font("../carmen_final_game_project/photo/score_font/Amatic-Bold.ttf", 25)
        high_score_text = high_score_font.render("High Score: " +str(high_score), True, white)
        high_score_rect = high_score_text.get_rect()
        high_score_rect.center = (screen_width//2, 130)
        screen.blit(high_score_text, high_score_rect)


    pygame.display.update()

    while gameover:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = False
                running = False
            #click to restart
            if event.type == pygame.MOUSEBUTTONDOWN:
                gameover = False
                speed = 2
                score = 0
                vehicle_group.empty()
                player.rect.center = [player_x, player_y]

