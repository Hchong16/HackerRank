# Author: Harry Chong
# Date: 09/05/2020
# Problem: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {")":"(", "}":"{", "]":"["}
        
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False

        return stack == []