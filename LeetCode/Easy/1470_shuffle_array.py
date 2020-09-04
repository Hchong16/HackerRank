# Author: Harry Chong
# Date: 09/03/2020
# Problem: https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = list()
        
        for i in range(0, n):
            result.append(nums[i])
            result.append(nums[i+n])
            
        return result