# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:58:49 2024

@author: Musaddique
"""

# basic_operations.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
