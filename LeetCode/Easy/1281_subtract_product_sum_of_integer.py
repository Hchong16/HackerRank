# Author: Harry Chong
# Date: 09/04/2020
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        values = list(str(n)) # Seperate values into list 
        
        # Initialize product to 1 since 0 * x will be 0...
        product, sum, result = 1, 0, 0

        for num in values:
            product = product * int(num)
            sum = sum + int(num)
        
        result = product - sum
        return result