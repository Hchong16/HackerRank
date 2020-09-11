# Author: Harry Chong
# Date: 9/10/2020
# Problem: https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, str: str) -> int:
        # Check if value is valid 
        try:
            result = int(str)
        except:
            result = []
            str = str.strip()
            
            num = 0 # Flag to prevent any new addition of '-' and '+'
            status = 1 # Flag to indicate when to stop adding to result
            
            for index, value in enumerate(str):
                if (value == "-" or value == "+") and (status == 1) and (num == 0):
                    result.append(value)
                    num = 1
                elif (value in ('0','1','2','3','4','5','6','7','8','9')) and (status == 1):
                    result.append(value)
                    num = 1
                else:
                    status = 0
                    
            result = ''.join(result)
        
        # Edge Cases
        try:
            result = int(result)

            if result < -2**31: 
                return -2**31
            elif result > 2**31-1: 
                return 2**31-1
            else: 
                return result
        except:
            return 0