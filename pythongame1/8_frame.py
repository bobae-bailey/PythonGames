import pygame
##################################################################
pygame.init()

# Screen Size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption('Bobae Game')

# FPS
clock = pygame.time.Clock()

####################################################################

# Event loop
running = True
while running:
    dt = clock.tick(60)

    print('fps : ' + str(clock.get_fps()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    pygame.display.update()

# pygame End
pygame.quit()
