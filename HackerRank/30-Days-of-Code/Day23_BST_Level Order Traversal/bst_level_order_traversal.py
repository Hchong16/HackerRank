#!/bin/python3
# Author: Harry Chong
# Data: 8/30/2020
# Day 23: Binary Search Trees - Level-Order Traversal
## https://www.hackerrank.com/challenges/30-binary-trees

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        queue = [root]

        while queue:
            front = queue.pop(0)
            print(front.data, end=" ")
            if front.left: 
                queue.append(front.left)
            if front.right:
                queue.append(front.right)
                
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
