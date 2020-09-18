# Author: Harry Chong
# Date: 09/15/2020
# Problem: https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s)-1
        
        while i < j:
            # Skip whitespace/special characters
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
                
            if i < j and s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
            
        return True
