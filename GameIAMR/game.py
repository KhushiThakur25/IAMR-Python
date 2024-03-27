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


white = 255,255,255
red = 255,0,0
yellow = 255,255,0
w,h = 30,30

def homeScreen():
    font = pygame.font.SysFont(None,100)
    text = font.render("Welcome to the jungle..",True,yellow)

    font_2 = pygame.font.SysFont(None,70)
    text_2 = font_2.render("Press SPACE to start ..",True,white)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()
        screen.blit(bg,(0,0))
        screen.blit(text,(100,100))
        screen.blit(text_2,(250,300))
        pygame.display.update()



def score(counter):
    font = pygame.font.SysFont(None,30)
    text = font.render(f"Score:{counter}",True,yellow)

    screen.blit(text,(100,10))

def gameOver():
    font = pygame.font.SysFont(None,200)
    text = font.render("Game Over..",True,red)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        
        screen.blit(text,(100,100))
        pygame.display.update()

def drawSnake(snakeList):
    for i in range(len(snakeList)):
        pygame.draw.rect(screen,white,[snakeList[i][0],snakeList[i][1],w,h])
    


def game():
    frogX = random.randint(1,screenWidth-frogWidth)
    frogY = random.randint(1,screenHeight-frogHeight)
    x,y = 0,0
    move_x = 0
    move_y = 0
    speed = 2
    counter = 0

    snakeList = []
    snakeLength = 1
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
        score(counter)
        

        snakeRect = pygame.draw.rect(screen,white,[x,y,w,h])
        frogRect = pygame.Rect(frogX,frogY,frogWidth,frogHeight)
        x += move_x
        y += move_y

        snakeHead = []
        snakeHead.append(x)
        snakeHead.append(y)
        snakeList.append(snakeHead)
        drawSnake(snakeList)

        if len(snakeList) > snakeLength:
            del snakeList[0]
        
        if x > screenWidth:
            x = -w
        elif x < -w:
            x = screenWidth-w
        elif y > screenHeight:
            y = -h
        elif y < -h:
            y = screenHeight-h
        # y += 0.3

        if frogRect.colliderect(snakeRect):
            frogX = random.randint(1,screenWidth-frogWidth)
            frogY = random.randint(1,screenHeight-frogHeight)
            snakeLength += 30
            counter += 1

        for i in snakeList[:-1]:
            if i == snakeList[-1]:
                gameOver()

        pygame.display.flip()

homeScreen()