#!/bin/python3
# Author: Harry Chong
# Data: 5/17/2020
# Day 3: Intro to Conditional Statements
# https://www.hackerrank.com/challenges/30-conditional-statements/problem

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())

    if N % 2 != 0:
        print("Weird")
    elif N % 2 == 0 and 2 <= N <= 5:
        print("Not Weird")
    elif N % 2 == 0 and 6 <= N <= 20:
        print("Weird")
    elif N % 2 == 0 and N > 20:
        print ("Not Weird")
    