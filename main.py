import pygame, sys

# function to move laser away from ship and remove lasers from list when they pass top
def laser_update(laser_list, speed = 300):
    for rect in laser_list:
        rect.y -= speed * dt
        if rect.bottom < 0:
            laser_list.remove(rect)

# game init
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Asteroid Shooter')
clock = pygame.time.Clock()

# ship import
ship_surf = pygame.image.load('graphics/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
# background import
background = pygame.image.load('graphics/background.png').convert()
# laser import
laser_surf = pygame.image.load('graphics/laser.png').convert_alpha()
laser_list = []
#laser_rect = laser_surf.get_rect(midbottom = ship_rect.midtop)
# text import
font = pygame.font.Font('graphics/subatomic.ttf', 50) 
text_surf = font.render('Space', True, "White")
text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))

test_rect = pygame.Rect(100,200,400,500)

#Keeps the code going
while True: #Run forever -> Keeps the game running
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
        if event.type == pygame.MOUSEBUTTONDOWN:
            laser_rect = laser_surf.get_rect(midbottom = ship_rect.midtop)
            laser_list.append(laser_rect)
      
    # framerate limit
    dt = clock.tick(120) / 1000

    # mouse input
    ship_rect.center = pygame.mouse.get_pos()

    # update
    laser_update(laser_list)

    # drawing
    display_surface.fill((0,0,0))
    display_surface.blit(background, (0,0))

    display_surface.blit(text_surf, text_rect)
    pygame.draw.rect(display_surface, 'white', text_rect.inflate(30, 10), width = 2, border_radius = 5)
    
    # for loop that draws the laser surface where the rects are
    for rect in laser_list:
        display_surface.blit(laser_surf, rect)

    display_surface.blit(ship_surf, ship_rect)

    # draw the final frame
    pygame.display.update()