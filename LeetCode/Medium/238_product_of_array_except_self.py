# Author: Harry Chong
# Date: 09/05/2020
# Problem: https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Since division cannot be used, first loop forward to calculate product
        # before the current position. Then, loop backward to calculate product 
        # after the current position.
        
        # Take both array and multiply them together to get final answer
        
        # Example:
        # Forward:             # Backward:
        # 1 2 3 4                1 2 3 4
        # 1 1 2 6                24 12 4 1
        
        result = []
        product = 1
        for i in range(0, len(nums)):
            result.append(product)
            product = product * nums[i]
            
        product = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] = result[i] * product # Multiple new value with current value to get final answer
            product = product * nums[i]
            
        return result