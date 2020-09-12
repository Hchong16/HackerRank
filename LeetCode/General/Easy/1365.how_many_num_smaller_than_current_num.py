# Author: Harry Chong
# Date: 09/04/2020
# Problem: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sort = sorted(nums)
        dictionary = {} # Value in nums as key
        
        result = list()
        
        # Since array is sorted, the current position is 
        # the number of values smaller than current number.
        for i in range(len(nums)):
            if sort[i] not in dictionary:
                dictionary[sort[i]] = i
                
        # Use dictionary to reconstruct final result
        for i in range(len(nums)):
            result.append(dictionary[nums[i]])
                 
        return result
        """
        # Slow Method
        result = list()
    
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i != j:
                    if nums[j] < nums[i]:
                        count += 1
            result.append(count)
                
        return result
        """
    