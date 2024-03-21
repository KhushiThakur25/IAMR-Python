import pygame
import random
pygame.init()
screenWidth = 1000
screenHeight = 500
size = screenWidth,screenHeight
screen = pygame.display.set_mode(size)

bg = pygame.image.load('bgg.png')
fg = pygame.image.load('frog1.png')

frogWidth = fg.get_width()
frogHeight = fg.get_height()

frogX = random.randint(1,screenWidth-frogWidth)
frogY = random.randint(1,screenHeight-frogHeight)

white = 255,255,255
red = 255,0,0
x,y,w,h = 0,0,30,30
move_x = 0.2
move_y = 0.2
speed = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x += speed
                move_y = 0
            elif event.key == pygame.K_LEFT:
                move_x -= speed
                move_y = 0
            elif event.key == pygame.K_UP:
                move_x = 0
                move_y -= speed
            elif event.key == pygame.K_DOWN:
                move_x = 0
                move_y += speed
        else:
            move_x = 0
            move_y = 0    

            

    # screen.fill(red)
    screen.blit(bg,(0,0))
    screen.blit(fg,(frogX,frogY))

    snakeRect = pygame.draw.rect(screen,white,[x,y,w,h])
    x += move_x
    y += move_y
    if x > screenWidth:
        x = -w
    elif x < -w:
        x = screenWidth-w
    elif y > screenHeight:
        y = -h
    elif y < -h:
        y = screenHeight-h
    # y += 0.3
    pygame.display.flip()
