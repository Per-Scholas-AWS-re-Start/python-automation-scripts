#!/bin/env python3

# Script Name   : rm_duplicate_funtion.py
# Author(s)     : Abraham Musa
# Created       : 15 February 2021
# Last Modified : 15 February 2021
# Version       : 1.1
# Modifications : 
# Description   : 

def remove_duplicates(lista):
    lista2 = []
    if lista: 
        for item in lista:
            if item not in lista2: #is item in lista2 already?
                lista2.append(item)
    else:
        return lista
    return lista2
print remove_duplicates([1,2,3,3])