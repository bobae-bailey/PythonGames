import os
import pygame


pygame.init()

# Screen Size
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption('Bobae Pang')

# FPS
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__) #files location
image_path = os.path.join(current_path, 'images')


# background
background = pygame.image.load(os.path.join(image_path, 'background.png'))


# stage
stage = pygame.image.load(os.path.join(image_path, 'stage.png'))
stage_size = stage.get_rect().size
stage_height = stage_size[1]



# character
character = pygame.image.load(os.path.join(image_path, 'character.png'))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height





# Event loop
running = True
while running:
    dt = clock.tick(60)

    print('fps : ' + str(clock.get_fps()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()


pygame.time.delay(2000)

# pygame End
pygame.quit()
