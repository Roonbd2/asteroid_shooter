import pygame, sys
from random import randint, uniform

#FUNCTIONS
# function to move laser away from ship and remove lasers from list when they pass top
def laser_update(laser_list, speed = 300):
    for rect in laser_list:
        rect.y -= speed * dt
        if rect.bottom < 0:
            laser_list.remove(rect)

# function to display the score as time since pygame.init was called
def display_score():
    score_text = f"Score: {pygame.time.get_ticks() // 1000}"
    text_surf = font.render(score_text, True, "White")
    text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))
    display_surface.blit(text_surf, text_rect)
    pygame.draw.rect(display_surface, 'white', text_rect.inflate(30, 10), width = 2, border_radius = 5)

# function that checks if we are able to shoot yet
def laser_timer(can_shoot, duration = 500):
    if not can_shoot:
        current_time = pygame.time.get_ticks()
        if current_time - shoot_time > duration:
            can_shoot = True
    return can_shoot

#function to move meteors and change list
def meteor_update(meteor_list, speed = 300):
    for meteor_tuple in meteor_list:
        direction = meteor_tuple[1]
        meteor_rect = meteor_tuple[0]
        meteor_rect.center += direction * speed * dt
        if meteor_rect.top > WINDOW_HEIGHT:
            meteor_list.remove(meteor_tuple)

#GAME INIT
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Asteroid Shooter')
clock = pygame.time.Clock()

#IMPORTS
# ship import
ship_surf = pygame.image.load('graphics/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
# background import
background = pygame.image.load('graphics/background.png').convert()
# laser import
laser_surf = pygame.image.load('graphics/laser.png').convert_alpha()
laser_list = []
#meteor import
meteor_surf = pygame.image.load('graphics/meteor.png').convert_alpha()
meteor_list = []
#laser timer
can_shoot = True
shoot_time = None
# text import
font = pygame.font.Font('graphics/subatomic.ttf', 50)

#meteor timer
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 500)

#GAME LOOP
while True: #Run forever -> Keeps the game running
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
        #laser on mouse push
        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:
            #laser
            laser_rect = laser_surf.get_rect(midbottom = ship_rect.midtop)
            laser_list.append(laser_rect)
            #timer logic
            can_shoot = False
            shoot_time = pygame.time.get_ticks()
        #meteor spawn timer
        if event.type == meteor_timer:
            #random position
            x_pos = randint(-100,WINDOW_WIDTH + 100)
            y_pos = randint(-100,-50)
            #creating a rect
            meteor_rect = meteor_surf.get_rect(center =(x_pos,y_pos))

            #random direction
            direction = pygame.math.Vector2(uniform(-0.5,0.5),1)

            meteor_list.append((meteor_rect, direction))
            
    # framerate limit
    dt = clock.tick(120) / 1000

    # mouse input
    ship_rect.center = pygame.mouse.get_pos()

    # update
    laser_update(laser_list)
    meteor_update(meteor_list)
    can_shoot = laser_timer(can_shoot, 500)

    # meteor ship collisions
    for meteor_tuple in meteor_list:
        meteor_rect = meteor_tuple[0]
        if ship_rect.colliderect(meteor_rect):
            pygame.quit()
            sys.exit()

    # laser meteor collision
    for laser_rect in laser_list:
        for meteor_tuple in meteor_list:
            if laser_rect.colliderect(meteor_tuple[0]):
                meteor_list.remove(meteor_tuple)
                laser_list.remove(laser_rect)
    

    # drawing
    display_surface.fill((0,0,0))
    display_surface.blit(background, (0,0))

    display_score()

    # for loop that draws the laser surface where the rects are
    for rect in laser_list:
        display_surface.blit(laser_surf, rect)

    for meteor_tuple in meteor_list:
        display_surface.blit(meteor_surf, meteor_tuple[0])

    display_surface.blit(ship_surf, ship_rect)

    # draw the final frame
    pygame.display.update()