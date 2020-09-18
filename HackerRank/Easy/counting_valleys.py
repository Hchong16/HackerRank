#!/bin/python3
# Question: https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    altitude = 0
    status = 'sea-level'
    result = 0 # Valleys traversed

    # Ignore mountain since we don't care about it.
    for direction in path:
        if direction == 'U':
            altitude += 1
        else:
            altitude -= 1

        if altitude < 0 and status == 'sea-level':
            result += 1
            status = 'valley'
        elif altitude == 0:
            status = 'sea-level'

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
