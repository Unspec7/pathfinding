import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Maze')
clock = pygame.time.Clock()
crash = False

while not crash:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crash = True
    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()


"""import sys
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
    sys.exit(main())"""
