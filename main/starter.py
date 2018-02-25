import pygame
import pickle

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


gameDisplay = pygame.display.set_mode((displaywidth,displayheight))
pygame.display.set_caption('Maze')
clock = pygame.time.Clock()
crash = False

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


while not crash:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crash = True
    gameDisplay.fill(white)
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects("A bit Racey", largeText)
    TextRect.center = ((displaywidth / 2), (displayheight / 2))
    gameDisplay.blit(TextSurf, TextRect)
    for i in range(0, 100):
        for j in range(0, 100):

            pygame.draw.rect(gameDisplay, black, (i*7, j*7, 6, 6), 0)
    mouse = pygame.mouse.get_pos()

    for i in range(0, 25):
        if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, gray, (750, 30+i*25, 80, 20), 0)
            pygame.draw.rect(gameDisplay, gray, (850, 30+i*25, 80, 20), 0)

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