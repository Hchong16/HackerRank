# Author: Harry Chong
# Date: 09/10/2020
# Problem: https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {} # Key: Value, Data: Position
        
        for i in range(0, len(nums)):
            value = nums[i]
            compliment = target - value
            
            if compliment in dict.keys():
                return ([i, dict[compliment]])
            elif value not in dict.keys():
                dict[value] = i
            
        return []