# Author: Harry Chong
# Date: 09/05/2020
# Problem: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        decimal = 0
        
        while head:
            decimal = decimal*2 + head.val
            head = head.next
            
        return decimal