#!/bin/python3
# Author: Harry Chong
# Data: 8/30/2020
# Day 25: Running Time and Complexity
## https://www.hackerrank.com/challenges/30-running-time-and-complexity

# Enter your code here. Read input from STDIN. Print output to STDOUT
def isPrime(n):
    # True = PRim
    # Corner Cases:
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

cases = int(input())

for i in range(0, cases):
    value = int(input())
    status = isPrime(value)
    if status:
        print("Prime")
    else:
        print("Not prime")
