# Author: Harry Chong
# Date: 09/04/2020
# Problem: https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {} # Use dict to map value and position.
        
        for i in range(0, len(nums)):
            value = nums[i]
            compliment = target - value # Value needed to reach target
            
            if compliment in dictionary.keys():
                return [i, dictionary[compliment]]
            elif value not in dictionary.keys():
                dictionary[value] = i # Key is value, Position is the data