import pygame
import pickle
from mazegen import *

pygame.init()
displaywidth = 1280
displayheight = 720

black = (0, 0, 0)
white = (255, 255, 255)
gray = (180, 180, 180)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
maze = []

pickle_in = open("mazes.dat","rb")
mazes = pickle.load(pickle_in)
maze = mazes[0]
gameDisplay = pygame.display.set_mode((displaywidth,displayheight))
pygame.display.set_caption('Maze')
clock = pygame.time.Clock()
crash = False

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


while not crash:
    def button(msg, x, y, w, h, ic, ac, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

            if click[0] == 1 and action != None:
                action()
        else:
            pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

        smallText = pygame.font.SysFont("freesansbold", 14)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(textSurf, textRect)


    def getMaze(i):
        return mazes[i]


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crash = True
    gameDisplay.fill(white)
    for i in range(0, 100):
        for j in range(0, 100):
            if maze.all_nodes[i][j].wall:
                pygame.draw.rect(gameDisplay, black, (i*7, j*7, 6, 6), 0)
    mouse = pygame.mouse.get_pos()
    smallText = pygame.font.Font("freesansbold.ttf", 14)
    for i in range(0, 25):
        button("Map "+str(i), 750, 30+i*25, 80, 20, gray, green, getMaze(i))


    pygame.display.update()
    clock.tick(30)


pygame.quit()
quit()


