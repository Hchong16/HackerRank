#!/bin/python3
# Author: Harry Chong
# Data: 9/3/2020
# Day 29: Bitwise AND
## https://www.hackerrank.com/challenges/30-bitwise-and

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()
        n, k = int(nk[0]), int(nk[1])
    
        # 2 <= K <= N
        if (k-1 | k) <= n:
            print(k-1)
        else:
            print(k-2)

        """ 
        # Brute Force Method
        values = list()

        S = list()
        for i in range(1, n+1):
            S.append(i)

        for i in range(0, len(S)-1):
            for j in range(1, len(S)):
                if S[i] != S[j] and S[i] < S[j]:
                    A, B = S[i], S[j]
                    if A < B and (A & B < k):
                        values.append(A & B)

        print(max(values))
        """