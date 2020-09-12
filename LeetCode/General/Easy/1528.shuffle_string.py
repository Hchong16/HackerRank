# Author: Harry Chong
# Date: 09/04/2020
# Problem: https://leetcode.com/problems/shuffle-string/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = len(s)*[None]
        s = list(s)
        
        for i in range(len(indices)):
            result[indices[i]] = s[i]
        
        result = "".join(result)
        return result