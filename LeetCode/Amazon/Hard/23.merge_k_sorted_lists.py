# Author: Harry Chong
# Date: 09/14/2020
# Problem: https://leetcode.com/problems/merge-k-sorted-lists/
# Data Structure Type: Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return 
        elif len(lists) == 1:
            return lists[0]
        
        mid = len(lists)//2
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])

        return self.merge(l, r)

    def merge(self, l1, l2):
        dummy = curr = ListNode(-1)
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = ListNode(l1.val)
                curr = curr.next
                l1 = l1.next
            else:
                curr.next = ListNode(l2.val)
                curr = curr.next
                l2 = l2.next
        
        if l1:
            curr.next = l1
        else:
            curr.next = l2
            
        return dummy.next
                

# USING PRIORITY QUEUE
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = head = ListNode(-1)
        q = PriorityQueue()
        
        for l in lists:
            if l:
                q.put((l.val, l))
        
        while not q.empty():
            val, node = q.get()

            head.next = ListNode(val)
            head = head.next
            node = node.next
            
            if node:
                q.put((node.val, node))
                
        return dummy.next
                
            