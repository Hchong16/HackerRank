#!/bin/python3
# Author: Harry Chong
# Data: 8/29/2020
# Day 20: Sorting
# # https://www.hackerrank.com/challenges/30-sorting

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

# Write Your Code Here
# Track number of elements swapped during single array traversal
numberOfSwaps = 0

for i in range(0, n):
    for j in range(0, n-1):
        # Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j+1]):
            a[j], a[j+1] = a[j+1], a[j]
            numberOfSwaps = numberOfSwaps + 1

    if (numberOfSwaps == 0):
        break;

print("Array is sorted in {} swaps.".format(numberOfSwaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))