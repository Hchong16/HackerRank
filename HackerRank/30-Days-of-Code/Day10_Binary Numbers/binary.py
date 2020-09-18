#!/bin/python3
# Author: Harry Chong
# Data: 5/24/2020
# Day 10: Binary Numbers
# https://www.hackerrank.com/challenges/30-binary-numbers/

import math
import os
import random
import re
import sys

def DecimalToBinary(num): 
    if num > 1: 
        DecimalToBinary(math.floor(num / 2))
    stack.append(num % 2)

if __name__ == '__main__':
    n = int(input())

    stack = []
    DecimalToBinary(n)

    # Count consecutive 1's
    count = 0
    maximum = 0

    while stack:
        temp = stack.pop()
        if temp == 1:
            count = count + 1

            if count > maximum:
                # Record new count of consecutive 1's
                maximum = count 
        else:
            count = 0

    print(maximum)
