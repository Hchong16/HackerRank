# Author: Harry Chong
# Date: 09/03/2020
# Problem: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        compare_val = max(candies) - extraCandies

        for i in range(len(candies)):
            candies[i] = (candies[i] >= compare_val)

        return candies
                
        """
        # Brute Force
        result = list()
        position = 0
         
        while position < len(candies):
            temp_candies = list()
            for i in range(0, len(candies)):
                if i == position:
                    temp_candies.append(candies[i] + extraCandies)
                else:
                    temp_candies.append(candies[i])

            if temp_candies[position] == max(temp_candies):
                result.append(True)
            else:
                result.append(False)
                
            position += 1
        
        return result
        """