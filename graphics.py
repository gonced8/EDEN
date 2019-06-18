# Gonçalo
import sys, pygame, color, Class_World, movement
from Class_Being import *

def initialize_display():

    #x = input('Insira o tamanho X do display: (ex: 800)')
    #y = input('Insira o tamanho Y do display: (ex: 600] )')
    x=1200
    y=800

    display_size = [int(x), int(y)]

    # Initializes everything necessary for Pygame
    pygame.init()

    # Sets window's size
    gameDisplay = pygame.display.set_mode(display_size)

    # Draws the background in white
    gameDisplay.fill(color.white)

    # Sets window's name
    pygame.display.set_caption('EDEN')

    # Updates display
    pygame.display.update()

    # Starts the clock
    clock = pygame.time.Clock()

    return gameDisplay, clock


def draw_being(gameDisplay, world, being):

    display_size = gameDisplay.get_size()
    world_size = world.size()
    x = display_size[0]/world_size[1]
    y = display_size[1]/world_size[0]

    for elem in being.pos:
        points = ((x*elem[1], y*elem[0]), (x*elem[1], y*(elem[0]+1)), (x*(elem[1]+1), y*(elem[0]+1)), (x*(elem[1]+1), y*elem[0]))
        pygame.draw.polygon(gameDisplay, being.color, points)

    return


def draw_food(gameDisplay, world, food):

    display_size = gameDisplay.get_size()
    world_size = world.size()
    x = display_size[0] / world_size[1]
    y = display_size[1] / world_size[0]

    for elem in food.pos:
        points = ((x * elem[1], y * elem[0]), (x * elem[1], y * (elem[0] + 1)), (x * (elem[1] + 1), y * (elem[0] + 1)),
                  (x * (elem[1] + 1), y * elem[0]))
        pygame.draw.polygon(gameDisplay, food.color, points)

    return


def update(fps, clock):
    # Updates display
    pygame.display.update()
    # Sets the clock according to the fps
    clock.tick(fps)
    return


def close_display():
    # Terminates Pygame
    pygame.quit()


# Prototype - not important
def test():

    # Initializes everything necessary for Pygame
    pygame.init()

    # Windows size
    display_size=[800, 600]

    # Sets window's size
    gameDisplay = pygame.display.set_mode(display_size)
    # Sets window's name
    pygame.display.set_caption('EDEN')
    # Starts the clock
    clock = pygame.time.Clock()
    # Frames per second
    fps=30

    # Initializes being
    speed=200
    radius=5
    position = [20, 20]
    pygame.draw.circle(gameDisplay, color.black, list(map(int, position)), 5)

    # Condition to terminate program
    close = False

    while not close:

        # Analizes all users inputs/events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True

        # Draws the background in white
        gameDisplay.fill(color.white)

        # Updates the being's position
        position = movement.next_pos(position, speed, radius, fps, display_size)
        # Draws the being
        pygame.draw.circle(gameDisplay, color.black, list(map(int, position)), radius)

        # Updates display
        pygame.display.update()
        # Sets the clock according to the fps
        clock.tick(fps)

    # Terminates Pygame
    pygame.quit()
    # Terminates Python
    quit()

    return