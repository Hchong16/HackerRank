#!/bin/python3
# Author: Harry Chong
# Data: 9/3/2020
# Day 28: RegEx, Patterns, and Intro to Databases
## https://www.hackerrank.com/challenges/30-regex-patterns

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())

    email = list()

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]

        if(re.search('[a-z]+@gmail.com$', emailID)):
            emailID = emailID.split('@')
            email.append(firstName)

    email =sorted(email)
    for i in email:
        print(i)
