# Author: Harry Chong
# Date: 09/06/2020
# Problem: https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        max_global = nums[0]
        max_current = nums[0]
        
        for i in range(1, len(nums)):
            # Check max between current value and previous sub-array
            max_current = max(nums[i], max_current + nums[i])
            max_global = max(max_current, max_global)
            
        return max_global