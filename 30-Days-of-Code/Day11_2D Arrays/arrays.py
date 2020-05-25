#!/bin/python3
# Author: Harry Chong
# Data: 5/24/2020
# Day 11: 2D Arrays
# https://www.hackerrank.com/challenges/30-2d-arrays/

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []

    # Setup Array
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # Hold all hourglass values
    values = []

    # Search through Array for maximum hourglass
    # At most 3 rows/columns can support an hourglass
    for i in range(0, 4): # Row
        for j in range(0, 4): # Column 
            temp_sum = 0;

            # Top Row:                             
            temp_sum = (arr[i][j] + arr[i][j+1] + arr[i][j+2]         # Top Row
                      + arr[i+1][j+1]                                 # Middle Row
                      + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])  # Bottom Row
            
            values.append(temp_sum)

    print(max(values))
