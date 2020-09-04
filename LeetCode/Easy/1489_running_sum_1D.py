# Author: Harry Chong
# Date: 09/03/2020
# Problem: https://leetcode.com/problems/running-sum-of-1d-array/submissions/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        result = list()
        
        for i in range(0, len(nums)):
            sum = sum + nums[i]
            result.append(sum)
            
        return result