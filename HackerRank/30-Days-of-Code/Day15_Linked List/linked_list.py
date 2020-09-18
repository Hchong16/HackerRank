#!/bin/python3
# Author: Harry Chong
# Data: 8/28/2020
# Day 15: Linked List
# https://www.hackerrank.com/challenges/30-linked-list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
        new_node = Node(data)

        # Check if Linked List is empty
        if head is None:
            head = new_node
        else:
            # Traverse to the end of the Linked List
            temp = head
            while (temp.next):
                temp = temp.next

            # Set next pointer of last node to new_node
            temp.next = new_node
        return head

    #Complete this method

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  