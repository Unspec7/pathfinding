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

mazes = []

maze = []
gameDisplay = pygame.display.set_mode((displaywidth,displayheight))
pygame.display.set_caption('Maze')
clock = pygame.time.Clock()
crash = False


def setmaze(i):
    print("setting maze "+str(i))
    global mazes
    if mazes:
        global maze
        maze = mazes[i]


def makemazes():
    global mazes
    mazes = []
    for i in range (1, 51):
        my_graph = Graph(100)
        generatemaze()
        my_graph.represent()
        mazes.append(my_graph)
        print("Graph "+str(i)+" done")

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


while not crash:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crash = True
    gameDisplay.fill(white)
    if maze:
        for i in range(0, 100):
            for j in range(0, 100):
                if maze.master[i][j].wall:
                    pygame.draw.rect(gameDisplay, black, (i*7, j*7, 6, 6), 0)
        mouse = pygame.mouse.get_pos()
    for i in range(0, 25):
        mazebutton("Map "+str(i+1), 750, 30+i*25, 80, 20, gray, green, i)
        mazebutton("Map " + str(i+26), 850, 30 + i * 25, 80, 20, gray, green, i+25)

    button("New Mazes", 1000, 100, 100, 30, gray, blue, makemazes)
    button("Load Mazes", 1000, 150, 100, 30, gray, blue, loadmazes)
    pygame.display.update()
    clock.tick(30)


pygame.quit()
quit()


