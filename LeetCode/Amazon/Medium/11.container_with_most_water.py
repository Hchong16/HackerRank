# Author: Harry Chong
# Date: 9/11/2020
# Problem: https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            l, r = height[left], height[right]
            
            w = right - left # Width of container
            h = min(l, r) # Take the minimum height that can be supported between the two
            area = w * h

            if l < r:    
                left += 1
            else:
                right -= 1
                
            if area > max_area:
                max_area = area
            
        return max_area