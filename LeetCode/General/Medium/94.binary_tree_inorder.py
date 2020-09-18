# Author: Harry Chong
# Date: 9/17/2020
# Question: https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Inorder Traversal: Left -> Root -> Right
        # Recursive Method:
        if not root:
            return []
        
        order = []
        order += self.inorderTraversal(root.left)
        order.append(root.val)
        order += self.inorderTraversal(root.right)
                      
        return order
        
        """
        # Stack Method:
        order, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
                
            if not stack:
                return order
            
            node = stack.pop()
            order.append(node.val)
            root = node.right
        """