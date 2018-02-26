import os
import time

import pygame

from mazegen import *

pygame.init()
displaywidth = 1280
displayheight = 720
gameDisplay = pygame.display.set_mode((displaywidth, displayheight))

black = (0, 0, 0)
white = (255, 255, 255)
gray = (180, 180, 180)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
darkred = (180, 0, 0)
maze = []

mazes = []

pygame.display.set_caption('Maze')
clock = pygame.time.Clock()


def forwardsastar():
    print("do the thing")


def backwardsastar():
    print("do the other thing")


def setmaze(maze_number):
    print("Maze set to maze number " + str(maze_number + 1))
    global mazes
    if mazes:
        global maze
        maze = mazes[maze_number]


def makemazes():
    global mazes
    mazes = []
    pygame.display.set_caption('Maze(Generating)')
    for x in range(0, 50):
        graph = Graph(101)
        generatemaze(graph)
        mazes.append(graph)
        print("Maze " + str(x + 1) + " done")

    setmaze(0)
    print("Done generating 50 mazes")
    pygame.display.set_caption('Maze')
    pickle_out = open("mazes.dat", "wb")
    pickle.dump(mazes, pickle_out)
    pickle_out.close()


def mazebutton(msg, x, y, w, h, ic, ac, action=None):
    maze_mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > maze_mouse[0] > x and y + h > maze_mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action is not None:
            setmaze(action)
            time.sleep(.5)
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
    try:
        pickle_in = open("mazes.dat", "rb")
        global mazes
        mazes = pickle.load(pickle_in)
        pygame.display.set_caption('Maze(Mazes loaded)')
        setmaze(0)
    except FileNotFoundError:
        pygame.display.set_caption('Maze(No mazes to load)')


def button(msg, x, y, w, h, ic, ac, action=None):
    button_mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > button_mouse[0] > x and y + h > button_mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
            time.sleep(.5)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("freesansbold", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


while True:
    done = False
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

    if done:
        break

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

pygame.quit()
os._exit(0)
