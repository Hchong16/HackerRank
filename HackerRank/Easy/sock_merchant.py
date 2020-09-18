#!/bin/python3
# Question: https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sockDict = {}
    result = 0

    # Add sock count to Dictionary
    for sock in ar:
        if sock not in sockDict:
            sockDict[sock] = 1
        else:
            sockDict[sock] += 1
    
    # Determine how many pairs for each sock type
    for sock in sockDict:
        result += sockDict[sock] // 2 # Ignore remainder
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')
    fptr.close()