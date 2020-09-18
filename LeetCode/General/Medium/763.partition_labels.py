# Author: Harry Chong
# Date: 09/13/2020
# Problem: https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        lastIndex = {}
        partitionLength = []
        
        # Determine last position found for each character in S
        for position, char in enumerate(S):
            lastIndex[char] = position
            
        print(lastIndex)    
            
        start = end = 0
        for position, char in enumerate(S):
            end = max(end, lastIndex[char])

            if position == end:
                partitionLength.append(position - start + 1)
                # Start New Partition
                start = position + 1
                
        return partitionLength
            