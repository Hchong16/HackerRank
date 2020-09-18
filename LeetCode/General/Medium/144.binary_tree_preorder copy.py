# Author: Harry Chong
# Date: 9/17/2020
# Question: https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Preorder: Root -> Left -> Right
        # Recursive Method:
        if root is None:
            return []
        
        order = [root.val]
        
        if root.left:
            order += self.preorderTraversal(root.left)
        if root.right:
            order += self.preorderTraversal(root.right)
            
        return order
        
        """
        ## Stack Method:
        if root is None:
            return []
        
        order, stack = [], [root]
        
        while stack:
            node = stack.pop()
            order.append(node.val)
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return order
        """