# Author: Harry Chong
# Date: 09/03/2020
# Problem: https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        
        for i in range(0, len(nums)-1):
            for j in range(0, len(nums)):
                if nums[i] == nums[j] and i < j:
                    result += 1
                    
        return result