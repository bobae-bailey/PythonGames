import pygame

pygame.init()

# Game Size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_width))

# Game Title
pygame.display.set_caption('Bobae Game')


# Event loop
running = True 
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
  

# pygame End
pygame.quit()