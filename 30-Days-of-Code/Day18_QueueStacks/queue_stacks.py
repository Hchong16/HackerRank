#!/bin/python3
# Author: Harry Chong
# Data: 8/28/2020
# Day 18: Interfaces
# # https://www.hackerrank.com/challenges/30-interfaces

import sys

class Solution:
    stack = []
    queue = []

    # Write your code here
    # [STACK]
    def pushCharacter(self, s):
        self.stack.append(s)
    def popCharacter(self):
        char = self.stack.pop()  #Remove Last (LIFO)
        return char 
    
    # [QUEUE]
    def enqueueCharacter(self, s):
        self.queue.append(s) 
    def dequeueCharacter(self):
        char = self.queue.pop(0) #Remove first
        return char

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    

