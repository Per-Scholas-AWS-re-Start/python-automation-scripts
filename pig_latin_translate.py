#!/bin/env python3

# Script Name   : ping_servers.py
# Author(s)     : Abraham Musa
# Created       : 15 February 2021
# Last Modified : 15 February 2021
# Version       : 1.1
# Modifications : 
# Description	 : 


#servers associated with that application group.

#Take the users input
words = raw_input("Enter some text to translate to pig latin: ")
print "You entered: ", words

#Now I need to break apart the words into a list
words = words.split(' ')

#Now words is a list, so I can manipulate each one usinga loop

for i in words:
    if len(i) >= 3: #I only want to translate words greater than 3 characters
        i = i + "%say" % (i[0]) 
        i = i[1:]
        print i
    else:
        pass