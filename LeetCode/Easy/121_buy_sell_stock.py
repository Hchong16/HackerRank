# Author: Harry Chong
# Date: 09/04/2020
# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit = 0
        
        for value in prices:
            if value < minPrice:
                minPrice = value
            elif value - minPrice > maxProfit:
                maxProfit = value - minPrice
            
        return maxProfit