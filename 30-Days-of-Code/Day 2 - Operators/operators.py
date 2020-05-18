 #!/bin/python3
# Author: Harry Chong
# Data: 5/17/2020
# Day 2: Operators
# https://www.hackerrank.com/challenges/30-operators/problem

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * tip_percent/100 
    tax = meal_cost * tax_percent/100
    totalCost = round(meal_cost + tip + tax)
    print(totalCost)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
