#!/bin/python3
# Author: Harry Chong
# Data: 5/17/2020
# Day 4: Class vs. Instance
# https://www.hackerrank.com/challenges/30-class-vs-instance/problem

import os
import sys

class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge > 0:
            self.age = initialAge 
        else:
            self.age = 0
            print("Age is not valid, setting age to 0.")

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print("You are young.")
        elif 13 <= self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        # Increment the age of the person in here
        self.age = self.age + 1

t = int(input())

# Test Code: [Uncomment for local test]
"""
person = Person(12)
person.amIOld()
person.yearPasses()
person.amIOld()
"""
