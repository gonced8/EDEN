#Project EDEN 13/12/2016 João Bernardino

from random import randint
from Class_World import *
from Class_Population import *
from prob import *
from color import *
from shape_generator import *
from Class_Food import *

class Being(object):
    """This class contains all the information that a being requires to exist"""
    """Every being has the following characteristics:
    -Position: this array represents the position of the being in the environment. Generally the environment is represented by a matrix MxN where we can find this being in the position [i,j]
    -Gender: male is represented by a 1 and female by a 0
    -Age: has the age of the being
    -Happiness: this value represents how happy said being is in a given moment of time, which is directly related to the satisfaction of its needs
    -Size: this value represents how big an individual is, 0
    -Speed: value that ranges from 0 to 255 that represents how fast a being can move, 0 being the slowest and 255 the fastest
    -Stamina: value that ranges from 0 to 255, representing how much stamina said being has
    -Aggressiveness: value that ranges from 0 to 255 showing how agressive the being is, 0 being the least and 255 the maximum
    -Perception: value that ranges from 0 to 255 informing how well the being can sense what's around him
    -Health: value that ranges from 0 to 255 saying how healthy the being is, 255 being max health

    Speed is directly related to health, age, agressivness, stamina, size and gender
    Stamina is directly related to hapinness and size
    Aggressiveness is directly related to happiness
    Perception is direclty related to age """
    
    def __init__(self, name, pos, gender, happiness, size, speed, stamina, agressiveness, perception, health, color):
        self.name = name
        self.pos= pos
        self.gender = gender
        self.age = 0
        self.happiness = happiness
        self.size = size
        self.speed = speed
        self.stamina = stamina
        self.aggressiveness = agressiveness
        self.perception = perception
        self.health = health
        self.color = color


    def show_being(self):
        print(" Name: {0} \n Position: {1} \n Gender: {2} \n Age: {3} \n Happiness: {4} \n Size: {5} \n Speed: {6} \n Stamina: {7} \n Aggressiveness: {8} \n Perception: {9} \n Health: {10} \n".format(
            self.name, self.pos, self.gender, self.age, self.happiness, self.size, self.speed, self.stamina, self.aggressiveness, self.perception, self.health))


    def eat(self, food, food_list, world):
        for elem in food:
            food_list.remove(elem, world)


#a=Being("a", [0,0] , random(), genrandom(255), genrandom(255), genrandom(255), genrandom(255), genrandom(255), genrandom(255), genrandom(255))
#a.show_being()


def perception_age(age, averagedeath):
    """Recieves the age of the being and the average death of the beings and returns a scalar showing how much vision impairment he should have
    The polynomial was calculted doing a quadratic regression of % of vision impairment vs how much he has lived in percentage"""
    normal_age=age/averagedeath #how much the being has lived in percentage
    if(age<(averagedeath*0.6)):
        return 1
    else:
        return (-0.864171428571437*((normal_age)^2)+1.288142857142878*normal_age+0.530714285714274)

def random_being(being_name,world,population):
    name=being_name
    size = randint(1, 50)
    position = generate_shape(size)
    position=rand_free_pos(world, position)
    population.add(Being(name,position,berprob(0.5),randint(0,255), size,randint(9,100)/10,randint(0,255),randint(0,255),randint(0,255), randint(0, 255), random_color()))
    insert_being(world, population.at(-1), population.at(-1).pos)
