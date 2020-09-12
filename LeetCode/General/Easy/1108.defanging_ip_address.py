# Author: Harry Chong
# Date: 09/03/2020
# Problem: https://leetcode.com/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = address.replace(".", "[.]")
        
        return result
        
        """
        #Brute Force
        ip = list(address)
        
        for i in range(len(ip)):
            if ip[i] == ".":
                ip[i] = "[.]"
        return ''.join(ip)
        """
        
        