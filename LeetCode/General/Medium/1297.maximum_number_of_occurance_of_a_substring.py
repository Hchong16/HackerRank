# Author: Harry Chong
# Date: 09/14/2020
# Problem: https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/
# Data Structure Type: Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        occurance = collections.defaultdict(int) # default value of int is 0
        
        # Perform Sliding Window
        for index in range(len(s) - minSize + 1):
            substring = s[index:index+minSize]
            
            # Set to determine number of unique numbers
            if(len(set(substring)) <= maxLetters):
                occurance[substring] += 1
                
        try:
            return max(occurance.values())
        except:
            return 0