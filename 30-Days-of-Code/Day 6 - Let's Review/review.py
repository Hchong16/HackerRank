#!/bin/python3
# Author: Harry Chong
# Data: 5/17/2020
# Day 6: Let's Review
# https://www.hackerrank.com/challenges/30-review-loop/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import os

if __name__ == '__main__':
    T = int(input()) # Number of Test Cases

    for i in range(0, T):
        S = str(input())
        N = len(S)

        even_string = ""
        odd_string = ""

        for i in range(0, N):
            if i % 2 == 0:
                even_string = even_string + S[i]
            else:
                odd_string = odd_string + S[i]

        print(even_string + " " + odd_string)
