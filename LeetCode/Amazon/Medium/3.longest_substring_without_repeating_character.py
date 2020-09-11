# Author: Harry Chong
# Date: 09/10/2020
# Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(k), where k is the length of the longest substring w/o repeating characters
        
        chars = set()
        left, right = 0, 0
        longest = 0
        
        while right < len(s):
            if s[right] not in chars:
                chars.add(s[right])
                right += 1
                longest = max(longest, right - left)
            else:
                chars.remove(s[left])
                left += 1
                
        return longest