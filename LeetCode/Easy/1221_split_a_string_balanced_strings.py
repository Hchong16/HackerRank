# Author: Harry Chong
# Date: 09/05/2020
# Problem: https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance, result = 0, 0
        
        for i in s:
            if i =="L":
                balance -= 1
            else:
                balance += 1
                
            if balance == 0:
                result += 1
                
        return result