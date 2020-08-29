#!/bin/python3
# Author: Harry Chong
# Data: 8/28/2020
# Day 16: Exceptions - String to Integer
# # https://www.hackerrank.com/challenges/30-exceptions-string-to-integer

import sys

S = input().strip()

try:
    value = int(S)
    print(value)
except:
    print("Bad String")