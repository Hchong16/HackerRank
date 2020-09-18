#!/bin/python3
# Author: Harry Chong
# Data: 5/17/2020
# Day 7: Arrays
# https://www.hackerrank.com/challenges/30-arrays/problem

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip( ).split()))

    print(" ".join(map(str, arr[::-1])))
    