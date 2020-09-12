# Author: Harry Chong
# Date: 09/07/2020
# Problem: https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            start = i + 1
            end = len(nums) - 1

            while start < end:
                sum = nums[i] + nums[start] + nums[end]

                if sum == 0:
                    result.add((nums[i], nums[start], nums[end]))
                    start += 1

                    # Remove Duplicates
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                elif sum < 0:
                    start += 1
                else:
                    end -= 1
            
        return result
        