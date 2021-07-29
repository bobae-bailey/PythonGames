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

# Character's moving direction
character_to_x = 0

# Character's moving speed
character_speed = 5

# Make the weapon
weapon = pygame.image.load(os.path.join(image_path, 'weapon.png'))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# multiple shot in one time
weapons = []

# weapon speed
weapon_speed = 10




# Event loop
running = True
while running:
    dt = clock.tick(60)

    print('fps : ' + str(clock.get_fps()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE: # shot the weapon
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
                

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
         character_x_pos = screen_width - character_width

    # weapons position

    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons] # make the weapon go up

    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]


    # showing on the screen

    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))


    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    
    pygame.display.update()


pygame.time.delay(2000)

# pygame End
pygame.quit()
