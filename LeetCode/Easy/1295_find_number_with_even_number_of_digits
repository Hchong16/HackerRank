# Author: Harry Chong
# Date: 09/05/2020
# Problem: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        
        for i in nums:
            temp = list(str(i))
            
            if len(temp) % 2 == 0:
                result += 1
        
        return result
            