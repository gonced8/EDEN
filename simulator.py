from graphics import *
from Class_World import *
from movement import *
from Class_Being import *
from Class_Population import *
from Class_Food import *

def simulator():

    #M=input('Insira o tamanho M do mundo: \ (ex: 100)')
    #N=input('Insira o tamanho N do mundo: \ (ex: 100)')
    M=300
    N=400

    world=World(int(M),int(N))
    population=Population()

    gameDisplay, clock = initialize_display()

    fps=10

    close = False

    for i in range(50):
        being_name="b"+str(i)
        random_being(being_name,world,population)

    food_count=0
    food_amount = 200

    food_list = Food_List(food_amount)

    while not close:

        # Analizes all users inputs/events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True

        # Draws the background in white
        gameDisplay.fill(color.white)

        # Refreshes the amount of food
        food_count = refresh_food(world, food_list)

        for food in food_list.list:
            draw_food(gameDisplay, world, food)

        for n in range(population.size()):

            being_name=population.at(n)

            # Updates the being's position
            next_pos(being_name, population, world, food_list)

            draw_being(gameDisplay, world, being_name)

        # Updates display
        update(fps, clock)

        #input()

    # Terminates Pygame
    close_display()
    # Terminates Python
    quit()

simulator()