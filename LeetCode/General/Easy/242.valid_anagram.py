# Author: Harry Chong
# Date: 09/04/2020
# Problem: https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # One Liner:
        #return sorted(s) == sorted(t)
    
        # Dictionary Method
        letter_count = {}
        
        # Must be same size if it is an anagram
        if len(s) != len(t): 
            return False
        
        # Iterate for string s
        for char in s:
            if char in letter_count.keys():
                letter_count[char] += 1
            else:
                letter_count[char] = 1
            
        # Iterate for string t
        for char in t:
            if char in letter_count.keys():
                letter_count[char] -= 1
            else:
                return False
            
        # Check letter dictionary results
        for i in letter_count.values():
            if i != 0:
                return False

        return True

        
        








