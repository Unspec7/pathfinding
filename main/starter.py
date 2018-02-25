import pygame
import sys
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
darkred = (180, 0, 0)
maze = []

mazes = []

gameDisplay = pygame.display.set_mode((displaywidth,displayheight))
pygame.display.set_caption('Maze')
clock = pygame.time.Clock()
crash = False


def forwardsastar():
    print("do the thing")


def backwardsastar( ):
    print("do the other thing")


def setmaze(i):
    print("setting maze "+str(i))
    global mazes
    if mazes:
        global maze
        maze = mazes[i]


def makemazes():
    global mazes
    mazes = []
    pygame.display.set_caption('Maze(Generating)')
    for i in range(0, 50):
        pygame.event.get()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        my_graph = Graph(101)
        generatemaze(my_graph)
        mazes.append(my_graph)
        print("Maze " + str(i+1) + " done")

    setmaze(0)
    print("Done generating 50 mazes")
    pygame.display.set_caption('Maze')
    pickle_out = open("mazes.dat", "wb")
    pickle.dump(mazes, pickle_out)
    pickle_out.close()


def mazebutton(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            setmaze(action)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("freesansbold", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def loadmazes():
    pickle_in = open("mazes.dat", "rb")
    global mazes
    mazes = pickle.load(pickle_in)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("freesansbold", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


while True:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    gameDisplay.fill(white)
    if maze:
        for i in range(0, 100):
            for j in range(0, 100):
                if maze.master[i][j].wall:
                    pygame.draw.rect(gameDisplay, black, (i*7, j*7, 6, 6), 0)
    for i in range(0, 25):
        mazebutton("Map "+str(i+1), 750, 30+i*25, 80, 20, gray, green, i)
        mazebutton("Map " + str(i+26), 850, 30 + i * 25, 80, 20, gray, green, i+25)

    button("Create Mazes", 1000, 100, 100, 30, gray, blue, makemazes)
    button("Load Mazes", 1000, 150, 100, 30, gray, blue, loadmazes)
    button("Forwards A*", 1000, 400, 100, 50, red, darkred, forwardsastar)
    button("Backwards A*", 1000, 500, 100, 50, red, darkred, backwardsastar)

    pygame.display.update()
    clock.tick(60)


