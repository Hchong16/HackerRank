# Author: Harry Chong
# Date: 09/05/2020
# Problem: https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.sum = 0
        
        def depth(node):
            # Not Null
            if node:
                if L < node.val:
                    depth(node.left)
                    
                if R > node.val:
                    depth(node.right)
                
                if node.val <= R and node.val >= L:
                    self.sum += node.val
                    
        depth(root)
        return self.sum