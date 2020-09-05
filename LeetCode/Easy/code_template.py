# Author: Harry Chong
# Date: 09/05/2020
# Problem: https://leetcode.com/problems/to-lower-case/

class Solution:
    def toLowerCase(self, str: str) -> str:
        result = ""
        
        # 65-90 A-Z; add 32 to get the lower case version (97-102 a-z)
        for char in str:
            if ord(char) >= 65 and ord(char) <= 90:
                result += chr(ord(char) + 32)
            else:
                result += char
                
        return result
            