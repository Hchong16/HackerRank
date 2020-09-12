# Author: Harry Chong
# Date: 09/04/2020
# Problem: https://leetcode.com/problems/create-target-array-in-the-given-order/

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = list()
        
        for i in range(0, len(index)):
            target.insert(index[i], nums[i])
            
        return target