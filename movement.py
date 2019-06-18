#Gonçalo
from math import cos, sin, radians
from random import randint
from Class_Being import *
from Class_World import *


# Calculation of next position
def next_pos(being, population, world, food_list):

    world_size = world.size()
    position=being.pos
    speed=being.speed
    # Sets a random angle of direction between 0º and 360º
    angle = radians(randint(0, 359))
    # Converts the angle to the proper x and y components
    direction = [cos(angle), sin(angle)]
    # Sets the time division accordingly to the fps
    dt=1.0
    # Calculates the amount to move
    dpos = list(map(int, [speed*direction[0]*dt, speed*direction[1]*dt]))
    # Updates position
    next_position = update_position(position, dpos, world_size)

    if not occupied(being, world, next_position):
        food = check_food(world, next_position)
        if len(food)>0:
            being.eat(food, food_list, world)

        update_world(world, being, next_position)
        being.pos=next_position


# The sum of two different lists
def update_position(points, dpos, world_size):

    final= []
    size = len(points)

    for elem in points:
        newpos = [elem[0]+dpos[0], elem[1]+dpos[1]]
        while (through(newpos, world_size)):
            continue
        final.append(newpos)

    return final


def occupied (being, world, points):
    world_size = world.size()
    for pos in points:
        if occupied_being(world, being, pos):
            return True
    return False


# Accordingly to this function, the being bounces on the surfaces of the window
def bounce(position, radius, display_size):
    if(position[0]<radius):
        position.insert(1, radius+(radius-position[0]))
        position.pop(0)
        return True

    elif(position[0]>display_size[0]-radius):
        position.insert(1, display_size[0]-radius-(position[0]-(display_size[0]-radius)))
        position.pop(0)
        return True

    elif(position[1]-radius<0):
        position.insert(1, radius+(radius-position[1]))
        position.pop(2)
        return True

    elif(position[1]+radius>display_size[1]):
        position.insert(1, display_size[0]-radius-(position[1]-(display_size[1]-radius)))
        position.pop(2)
        return True

    else:
        return False
