# Author: Harry Chong
# Date: 09/14/2020
# Problem: https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/

class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        left_sum, right_sum = 0, sum(nums)
        
        nums.sort(reverse=True)
        
        for index, num in enumerate(nums):
            left_sum += num
            right_sum -= num
            
            if left_sum > right_sum:
                return nums[:index + 1]