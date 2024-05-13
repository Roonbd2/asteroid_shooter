import pygame, sys

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
laser_rect = laser_surf.get_rect(midbottom = ship_rect.midtop)

# text import
font = pygame.font.Font('graphics/subatomic.ttf', 50) 
text_surf = font.render('Space', True, "White")
text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))

#Keeps the code going
while True: #Run forever -> Keeps the game running
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
      
    # framerate limit
    clock.tick(60)

    # mouse input
    ship_rect.center = pygame.mouse.get_pos()

    # update
    laser_rect.y -= 10

    # drawing
    display_surface.fill((0,0,0))
    display_surface.blit(background, (0,0))   
    display_surface.blit(ship_surf, ship_rect)
    display_surface.blit(text_surf, text_rect)
    display_surface.blit(laser_surf, laser_rect)

    # draw the final frame
    pygame.display.update()