import pygame

pygame.init()
displaywidth = 800
displayheight = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
maze =

gameDisplay = pygame.display.set_mode((displaywidth,displayheight))
pygame.display.set_caption('Maze')
clock = pygame.time.Clock()
crash = False




while not crash:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crash = True
    gameDisplay.fill(white)
    for i in range(0, 10):
        for j in range(0, 10):
            if maze(i, j).block is True:
                pygame.draw.rect(gameDisplay, black, (i*5, j*5, 5, 5), 0)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()


"""import sys
import sys
import getopt


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error as msg:
            raise Usage(msg)

        #launchAstarshithere()

    except Usage as err:
        print >> sys.stderr, err.msg
        print >> sys.stderr, "for help use --help"
        return 2


if __name__ == "__main__":
    sys.exit(main())
"""