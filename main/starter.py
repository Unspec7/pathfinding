import os
import time
import ctypes
import pygame
from astar import *
from mazegen import *

pygame.init()
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
displaywidth, displayheight = int(user32.GetSystemMetrics(0)*.75), int(user32.GetSystemMetrics(1)*.75)

# Ensure game screen is big enough
if displaywidth < 1440 or displayheight < 810:
    displaywidth = 1440
    displayheight = 810

gameDisplay = pygame.display.set_mode((displaywidth, displayheight))

print(pygame.font.get_fonts())
black = (0, 0, 0)
white = (255, 255, 255)
gray = (180, 180, 180)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
darkred = (180, 0, 0)
maze_area = pygame.draw.rect(gameDisplay, red, (0, 0, 808, 808), 0)
sink = []
maze = []
mazes = []

pygame.display.set_caption('Maze(No mazes loaded)')

clock = pygame.time.Clock()


def forwardsastar():
    global maze
    if maze:
        pygame.display.set_caption('Maze(Running forward A*)')
        if maze.need_clean:

            print("Cleaning")
            maze.clean()
            search(maze)
            #a_star_search(maze)
        else:
            maze.clean()
            #a_star_search(maze)
            print("Didn't need cleaning")
            search(maze)
            #a_star_search(maze)
        if maze.path_found is False:
            pygame.display.set_caption('Maze(No possible path)')
        else:
            global sink
            sink = maze.master[100][100]
            pygame.display.set_caption('Maze(Path found, updating display...)')
            update_image(maze.path_found)
            pygame.display.set_caption('Maze(Path found)')
    else:
        pygame.display.set_caption('Maze(No mazes available)')


def backwardsastar():
    global maze
    if mazes:
        pygame.display.set_caption('Maze(Running reverse A*)')
        if maze.need_clean:
            print("Cleaning")
            maze.clean()
            a_star_backwards(maze)
        else:
            print("Didn't need cleaning")
            a_star_backwards(maze)
        if maze.path_found is False:
            pygame.display.set_caption('Maze(No possible path)')
        else:
            global sink
            sink = maze.master[0][0]
            pygame.display.set_caption('Maze(Path found, updating display...)')
            update_image(maze.path_found)
            pygame.display.set_caption('Maze(Path found)')
    else:
        pygame.display.set_caption('Maze(No mazes available)')


def setmaze(maze_number):
    global mazes
    if mazes:
        global maze
        maze = mazes[maze_number]
        pygame.display.set_caption('Maze(Updating display...)')
        update_image(maze.path_found)
        pygame.display.set_caption('Maze(Maze number ' + str(maze_number + 1) + ')')
    else:
        pygame.display.set_caption('Maze(No mazes available)')


def makemazes():
    global mazes
    mazes = []
    pygame.display.set_caption('Maze(Generating)')
    for x in range(0, 50):
        # So it doesn't go into not responding mode
        pygame.event.get()
        graph = Graph(101)
        generatemaze(graph)
        mazes.append(graph)
        pygame.display.set_caption("Maze(Generating maze number " + str(x + 1) + " )")

    pygame.display.set_caption('Maze(Mazes generated)')
    setmaze(0)
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
    pygame.display.set_caption('Maze(Loading mazes...)')
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

    smallText = pygame.font.SysFont("'verdana'", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def update_image(ran):
    gameDisplay.fill(white, maze_area)
    for i in range(0, 101):
        for j in range(0, 101):
            if maze.master[i][j].wall:
                pygame.draw.rect(gameDisplay, black, (i * 8, j * 8, 7, 7), 0)

            # Only draw this stuff if we ran the thing
            if ran:
                if maze.master[i][j].searchvisit:
                    pygame.draw.rect(gameDisplay, green, (i * 8, j * 8, 7, 7), 0)
                global sink
                if sink:
                    iter = sink
                    while iter.parent:
                        pygame.draw.rect(gameDisplay, red, (iter.x * 8, iter.y * 8, 7, 7), 0)
                        iter = iter.parent

            if i == 0 and j == 0:
                pygame.draw.rect(gameDisplay, blue, (i * 8, j * 8, 7, 7), 0)
            elif i == 100 and j == 100:
                pygame.draw.rect(gameDisplay, gray, (i * 8, j * 8, 7, 7), 0)


def draw_buttons():
    for i in range(0, 25):
        mazebutton("Map " + str(i+1), 900, 30+i*25, 80, 20, gray, green, i)
        mazebutton("Map " + str(i+26), 1000, 30 + i * 25, 80, 20, gray, green, i+25)

    button("Generate Mazes", 900, 700, 200, 30, gray, blue, makemazes)
    button("Load Mazes", 900, 750, 200, 30, gray, blue, loadmazes)
    button("Forwards A*", 1150, 400, 150, 50, red, darkred, forwardsastar)
    button("Backwards A*", 1150, 500, 150, 50, red, darkred, backwardsastar)

gameDisplay.fill(white)
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

    draw_buttons()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
os._exit(0)
