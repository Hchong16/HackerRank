# Author: Harry Chong
# Date: 09/05/2020
# Problem: https://leetcode.com/problems/xor-operation-in-an-array/

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        # Time Complexity: O(n)
        result = start
        
        for i in range(1, n):
            result = result ^ start+2*i
        
        return result
        
        
        """
        # Time Complexity: O(2n)
        nums = list()
        result = 0
        
        # Generate Nums
        for i in range(0, n):
            nums.append(start + 2*i)
            
        for i in range(0, n):--
            result =  result ^ nums[i]
            
        return result
        """