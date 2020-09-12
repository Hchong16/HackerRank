# Author: Harry Chong
# Date: 09/04/2020
# Problem: https://leetcode.com/problems/decompress-run-length-encoded-list/
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = list()
        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i+1]
            
            # Python Function
            result.extend([val]*freq)
            
            # Brute Force
            #for i in range(0, freq):
            #    result.append(val)
                
        return result