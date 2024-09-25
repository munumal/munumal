# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 20:34:55 2024

@author: Musaddique
"""

# Geometry.py

def circle(radius):
    
    pi = 3.141592653589793
    area = pi * radius * radius
    perimeter = 2 * pi * radius
    print (f"For radius:{radius}")
    return (f"Area of circle : {area} \nCircumference of circle : {perimeter}\n")

def rectangle(length, width):
    
    area = length * width
    perimeter = 2 * (length + width)
    print (f"For Length :{length}, Width :{width}")
    return (f" Area of rectangle : {area} \nPerimeter of rectangle : {perimeter}\n")
    
    


