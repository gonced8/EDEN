from Class_World import *

class Population(object):
    """ This class is responsible for all the actions related to a world"""
    """ A world is represented by a matrix MxN in which each position may conain "0" or the name of the object in that
    position. Each function is described below."""

    # This function initializes an empty world M by N
    def __init__(self):
        self.population = []

    def print(self):
        print(self.population)

    # Returns
    def size(self):
        return len(self.population)

    # Inserts
    def add(self,being_name):
        self.population=self.population+[0]
        self.population[-1]=being_name

    # Removes
    def remove(self, world, being_name):
        new_population=[]
        world.remove_being(being_name)
        for element in self.population:
            if element is not being_name:
                new_population=new_population+[element]
        self.population=new_population

    def at(self,n):
        return self.population[n]


    def death(self,world):
        population_copy=self.population
        for element in population_copy:
            being_name=element
            health=being_name.health
            if health==0:
                self.remove(world, being_name)