# Author: Harry Chong
# Date: 09/12/2020
# Problem: https://leetcode.com/problems/merge-two-sorted-lists/
# Data Structure Type: Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        head = dummy
        
        while (l1 and l2):
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next

            dummy = dummy.next
        
        # Append remaining list
        if l1:
            dummy.next = l1
        else:
            dummy.next = l2
    
        return head.next