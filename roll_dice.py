#!/bin/env python3

# Script Name   : roll_dice.py
# Author(s)     : Abraham Musa
# Created       : 15 February 2021
# Last Modified : 15 February 2021
# Version       : 1.1
# Modifications : 
# Description   : 

import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print "Rolling the dices..."
    print "The values are...."
    print random.randint(min, max)
    print random.randint(min, max)

    roll_again = raw_input("Roll the dices again?")