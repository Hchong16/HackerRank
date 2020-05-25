#!/bin/python3
# Author: Harry Chong
# Data: 5/24/2020
# Day 9: Recursion 3
# https://www.hackerrank.com/challenges/30-recursion/

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    # Base Case
    if (n <= 1):
        return 1
    # Recursion Case
    else:
        return (n * factorial(n-1))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
