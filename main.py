import pygame, sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Asteroid Shooter')
clock = pygame.time.Clock()

#importing images
ship_surf = pygame.image.load('graphics/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

background = pygame.image.load('graphics/background.png').convert()

#import text
font = pygame.font.Font('graphics/subatomic.ttf', 50) 
text_surf = font.render('Space', True, "White")
text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))

#Keeps the code going
while True: #Run forever -> Keeps the game running
    # 1. Input -> Events(mouse clicks, mouse movements, press of button etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
   
    #framerate limit
    clock.tick(60)

    # 2. Updates
    display_surface.fill((0,0,0))
    display_surface.blit(background, (0,0))
    
    if ship_rect.top > 0:
        ship_rect.y -= 4     
    display_surface.blit(ship_surf, ship_rect)
    display_surface.blit(text_surf, text_rect)

    # 3. Show the frame to the player / update the display surface
    pygame.display.update()