# Author: Harry Chong
# Date: 09/04/2020
# Problem: https://leetcode.com/problems/xor-operation-in-an-array/

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = list()
        result = 0
        
        for i in range(0, n):
            nums.append(start + 2*i)
            
        for i in range(0, n):
            result =  result ^ nums[i]
            
        return result