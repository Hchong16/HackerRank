# Author: Harry Chong
# Date: 9/11/2020
# Problem: https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        dict = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}   

        result = ""
        
        for k in dict:
            while num >= k:
                result += (dict[k])
                num -= k
           
        return result