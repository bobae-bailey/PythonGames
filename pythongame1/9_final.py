import random
import pygame
###########################################################
pygame.init()

# This is a comment
# Screen Size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption('Quiz')

# FPS
clock = pygame.time.Clock()
###########################################################

background = pygame.image.load('./images/background.png')


dog =  pygame.image.load('./images/dog.png')
dog_size = dog.get_rect().size
dog_width = dog_size[0]
dog_height = dog_size[1]
dog_x_pos = (screen_width / 2) - (dog_width / 2)
dog_y_pos = screen_height - dog_height
to_x = 0
dog_speed = 10

#Enemy
poop = pygame.image.load('./images/poop.png')
poop_size = poop.get_rect().size
poop_width = poop_size[0]
poop_height = poop_size[1]
poop_x_pos = random.randint(0, screen_width - poop_width)
poop_y_pos = 0
poop_speed = 10

# Event loop
running = True
while running:
    dt = clock.tick(60)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= dog_speed
            elif event.key == pygame.K_RIGHT:
                to_x =+ dog_speed


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0


    dog_x_pos += to_x

    if dog_x_pos < 0:
        dog_x_pos = 0
    elif dog_x_pos > screen_width - dog_width:
        dog_x_pos = screen_width - dog_width

    poop_y_pos += poop_speed

    if poop_y_pos > screen_height:
        poop_y_pos = 0
        poop_x_pos = random.randint(0, screen_width - poop_width)

    dog_rect = dog.get_rect()
    dog_rect.left = dog_x_pos
    dog_rect.top = dog_y_pos

    poop_rect = poop.get_rect()
    poop_rect.left = poop_x_pos
    poop_rect.top = poop_y_pos

    if dog_rect.colliderect(poop_rect):
        print('I am crashed')
        running = False


    screen.blit(background, (0, 0))
    screen.blit(dog, (dog_x_pos, dog_y_pos))
    screen.blit(poop, (poop_x_pos, poop_y_pos))

    pygame.display.update()

pygame.time.delay(1000)



pygame.quit()
