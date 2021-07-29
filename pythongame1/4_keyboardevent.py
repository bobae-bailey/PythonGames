import pygame

pygame.init()

# Game Size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption('Bobae Game')

# Background
background = pygame.image.load('./images/background.png')

# character
character = pygame.image.load("./images/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height


to_x = 0
to_y = 0

# Event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



        if event.type == pygame.KEYDOWN:   # when you press the key
            if event.key == pygame.K_LEFT:
                to_x -= 1
            elif event.key == pygame.K_RIGHT:
                to_x += 1
            elif event.key == pygame.K_UP:
                to_y -= 1
            elif event.key == pygame.K_DOWN:
                to_y += 1

        if event.type == pygame.KEYUP:   # when you not press the key
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width


    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

        

    screen.blit(background, (0, 0))

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

# pygame End
pygame.quit()
