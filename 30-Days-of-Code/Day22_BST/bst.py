#!/bin/python3
# Author: Harry Chong
# Data: 8/30/2020
# Day 22: Binary Search Trees
## https://www.hackerrank.com/challenges/30-binary-search-trees

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

    def getHeight(self,root):
        
        #Write your code here
        if (root == None):
            return -1

        lft = self.getHeight(root.left)
        rht = self.getHeight(root.right)

        return(max(lft, rht) + 1)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       