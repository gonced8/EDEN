# Project EDEN 13/12/2016 - Afonso Raposo

from random import randint

class World(object):
    """ This class is responsible for all the actions related to a world"""
    """ A world is represented by a matrix MxN in which each position may conain "0" or the name of the object in that
    position. Each function is described below."""

    # This function initializes an empty world M by N
    def __init__(self, m, n):
        self.world = [[0]*n for _ in range(m)]

    # Prints a more beautiful version of world
    def print(self):
        for row in self.world:
            print(row)

    # Returns [M,N] in which M is the number of rows in world and N is the number of columns
    def size(self):
        return [len(self.world), len(self.world[0])]

    # Inserts an object in a chosen position [i,j].
    def insert(self, pos, obj):
        self.world[pos[0]][pos[1]] = obj

    # Removes any object from given position [i,j].
    def remove(self, pos):
        self.world[pos[0]][pos[1]] = 0

    # Returns True if given position [i,j] in world is free and returns False if not.
    def free_pos(self, pos):
        return self.world[pos[0]][pos[1]] == 0

    # Returns the name of what's in the position [pos].
    def what_in(self, pos):
        return self.world[pos[0]][pos[1]]

    # Show world the way it's implemented
    def show(self):
        return self.world

    def remove_being(self, being):
        for pos in being.pos:
            self.remove(pos)



# Determines if the position is occupied by a being different than the one in study
def occupied_being(world, being, position):
    obj = world.what_in(position)
    if type(obj) is str:
        if obj == being.name:
            return False
        else:
            return True


# Changes the being to the next position in world
def update_world(world, being, next_position):
    world.remove_being(being)
    insert_being(world, being, next_position)
    return


def rand_free_pos(world, points):
    ok=False
    world_size=world.size()

    while not ok:
        ok = True
        final = []
        i=randint(0,world_size[0]-1)
        j=randint(0,world_size[1]-1)
        for elem in points:
            pos = [i+elem[0], j+elem[1]]
            while(through(pos, world_size)):
                continue
            if not world.free_pos(pos):
                ok=False
                break
            final.append(pos)

    return final


def insert_being(world, being, points):
    for pos in points:
        world.insert(pos, being.name)



# Accordingly to this function, there are no boundaries. The left limit is the same as the right; and the down with the upper.
def through(position, world_size):

    if (position[0] < 0):
        position.insert(1, position[0]+world_size[0])
        position.pop(0)
        return True

    elif (position[0] >= world_size[0]):
        position.insert(1, position[0]-world_size[0])
        position.pop(0)
        return True

    elif (position[1] < 0):
        position.insert(1, position[1]+world_size[1])
        position.pop(2)
        return True

    elif (position[1] >= world_size[1]):
        position.insert(1, position[1]-world_size[1])
        position.pop(2)
        return True

    else:
        return False






"""
Import class:
    from Class_World import *

Create 3x3 world:
in    world=World(3,3)

Print world:
in    world.print()
out   0 0 0
      0 0 0
      0 0 0

Size world:
in    world.size()
out   [3,3]

Insert object in world in position [i,j]:
in    world.insert([0,0],obj)
in    world.print()
out   1 0 0
      0 0 0
      0 0 0

Is [i,j] a free position:
in    world.free_pos([0,0])
out   False

What is in position [i,j]:
in    world.what_in([0,0])
out   "1"

Remove an object from position [i,j]:
in    world.remove[0,0]
in    world.print()
out   0 0 0
      0 0 0
      0 0 0

See how world is implemented:
in    world.show()
out   [["0","0","0"],["0","0","0"],["0","0","0"]]

"""