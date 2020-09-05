# Author: Harry Chong
# Date: 09/04/2020
# Problem: https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        
        for i in nums:
            if i not in dictionary.keys():
                dictionary[i] = 1 # 1 is placeholder. We only care about the key
            else:
                return True
        
        return False
            