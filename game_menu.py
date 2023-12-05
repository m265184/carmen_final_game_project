import pygame




def display_menu():
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
    screen.blit(screen, (0, 0))

    Title_font = pygame.font.Font('../carmen_final_game_project/photo/score_font/custom_font.ttf', 64)
    Start_font = pygame.font.Font('../carmen_final_game_project/photo/score_font/custom_font.ttf', 60)
    Title = Title_font.render("Dodge Racers", True, (155, 155, 255))
    start = Start_font.render("Press enter to start", True, (155, 155, 255))
    screen.blit(Title, (screen_width/2 - Title.get_width()/2 , screen_height/2 - Title.get_height()/2))
    screen.blit(start, (screen_width/1.5 - start.get_width()/1.5, screen_height/1.5 - start.get_height()/1.5))


    #while Enter:
#        display_menu()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#             elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
#                 Enter = False
