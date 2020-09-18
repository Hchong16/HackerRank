#!/bin/python3
# Author: Harry Chong
# Data: 8/28/2020
# Day 19: Interfaces
# # https://www.hackerrank.com/challenges/30-interfaces

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        valList = []
        
        # Determine all divisible values
        for i in range(1, n + 1):
            if (n % i == 0):
                valList.append(i)

        # Calculate sum
        self.divisorSum = 0
        for i in range(0, len(valList)):
            self.divisorSum = self.divisorSum + valList[i]

        return self.divisorSum


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)