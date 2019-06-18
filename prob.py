# Project EDEN 13/12/2016 - Afonso Raposo and more to come

# This package contains functions related to probability

from random import random

# Function bindprob decides if given action with probability of occurring raging from 0 to 1 occurs or not, returning
# a binary value, 0 or 1.

def berprob(probability):
    if probability==0:
        return 0
    else:
        return int(random()<=probability)