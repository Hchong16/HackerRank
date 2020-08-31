#!/bin/python3
# Author: Harry Chong
# Data: 8/30/2020
# Day 24: More Linked Lists
## https://www.hackerrank.com/challenges/30-linked-list-deletion

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        unique = []
        current = head

        while(current):
            if current.data not in unique:
                unique.append(current.data)
                print(current.data, end=" ")
            else:
                temp = current.next
                current = temp


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 