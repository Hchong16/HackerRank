# Author: Harry Chong
# Date: 09/12/2020
# Problem: https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        
        result = 0
        
        for i in range(0, len(s) - 1):
            if dict[s[i]] < dict[s[i+1]]:
                result = result - dict[s[i]]
            else:
                result = result + dict[s[i]]

        
        return result + dict[s[-1]]