import pygame

pygame.init()

# Game Size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_width))

# Game Title
pygame.display.set_caption('Bobae Game')

# Background
background = pygame.image.load('./images/background.png')


# Event loop
running = True 
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
  

    screen.blit(background, (0, 0))

    pygame.display.update()

# pygame End
pygame.quit()