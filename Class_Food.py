from Class_World import *
from random import randint
from shape_generator import *
from color import *

#####################################################################################################

class Food(object):
    """ This class is responsible for every food that will be available in the simulation"""

    def __init__(self, type, pos, color):
        self.type = type
        self.pos = pos
        self.color = color

    def print(self):
        print("Type:", self.type)
        print("Position:", self.pos)
        print("Color:", self.color)

    def type(self):
        return self.type

    def pos(self):
        return self.pos

    def color(self):
        return self.color


#############################################################################################################

class Food_List(object):
    """ This class is responsible for a list of every food that will be available in the simulation"""

    def __init__(self, quantity):
        self.list = []
        self.quantity = quantity

    # This prints the list INCOMPLETE
    def print(self):
        print(self.list)

    def pos(self):
        for elem in self.list:
            print(elem.pos)

    # Returns
    def size(self):
        return len(self.list)

    # Inserts
    def add(self, food, world):
        self.list.append(food)
        for pos in food.pos:
            world.insert(pos, food)

    # Removes
    def remove(self, food, world):

        i=0
        for element in self.list:
            if element.pos is food.pos:
                self.list.pop(i)
            else:
                i=i+1

        '''

        new_list=[]
        for element in self.list:
            if element.pos is not food.pos:
                new_list=new_list+[element]
        self.list=new_list

        for pos in food.pos:
            world.remove(pos)

        '''

#########################################################################################################

def spawn_food (world, list, type, pos, size, color):
    if(len(type)==0):
        type = "food_simple"
    if len(pos)==0:
        position = generate_shape(size)
        position = rand_free_pos(world, position)
    if len(color)==0:
        color = random_color()

    food = Food(type, position, color)
    list.add(food, world)

    return food


def refresh_food (world, list):
    amount = list.quantity
    count = list.size()

    for count in range(count, amount):
        spawn_food(world, list, "", [], 1, green)

    return count+1


def check_food (world, points):
    food = []

    for position in points:
        obj = world.what_in(position)
        if type(obj) is Food:
            food.append(obj)

    return food