#!/bin/python3
# Author: Harry Chong
# Data: 5/17/2020
# Day 5: Loops
# https://www.hackerrank.com/challenges/30-loops/problem

import math
import os
import random
import re
import sys

def multiple(n):
    for i in range(1,11):
        result = n * i
        print("{} x {} = {}".format(n, i, result))

if __name__ == '__main__':
    n = int(input())
    multiple(n)
