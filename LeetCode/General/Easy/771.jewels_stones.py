# Author: Harry Chong
# Date: 09/03/2020
# Problem: https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        result = 0
        
        for char in S:
            if char in J:
                result += 1
                
        return result