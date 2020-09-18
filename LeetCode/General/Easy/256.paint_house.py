# Author: Harry Chong
# Date: 9/17/2020
# Question: https://leetcode.com/problems/paint-house/
# Dynamic Programming / Trees

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # Dynamic Programming
        # Calculate for 2nd to last row using last row. Calculate bottom to up
        for n in range(len(costs)-2, -1, -1):
            # Total cost of nth red house
            costs[n][0] += min(costs[n+1][1], costs[n+1][2])
            # Total cost of nth green house
            costs[n][1] += min(costs[n+1][0], costs[n+1][2])
            # Total cost of nth blue house
            costs[n][2] += min(costs[n+1][0], costs[n+1][1])
            
        if len(costs) == 0:
            return 0
        
        return min(costs[0]) # Return minimum in first row
    
            
        """
        # Memoization
        def paint_cost(n, color):
            if (n, color) in self.memo:
                return self.memo[(n, color)]
            
            total_cost = costs[n][color]
            if n == len(costs) - 1:
                pass
            elif color == 0: # RED (0)
                total_cost += min(paint_cost(n + 1, 1), paint_cost(n + 1, 2))
            elif color == 1: # GREEN (1)
                total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 2))
            else: # BLUE (2)
                total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 1))
            return total_cost
        
            self.memo[(n, color)] = total_cost
            return total_cost
        
        if costs == []:
            return 0
        
        self.memo = {}
        return min(paint_cost(0, 0), paint_cost(0, 1), paint_cost(0, 2))
        """