# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 15:00:11 2024

@author: Musaddique
"""

# advanced_operations.py

import math

def power(base, exponent):
    return base ** exponent

def square_root(number):
    if number < 0:
        raise ValueError("Cannot take the square root of a negative number!")
    return math.sqrt(number)
