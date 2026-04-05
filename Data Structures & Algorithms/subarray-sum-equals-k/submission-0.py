from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = 0
        prefix_map = {0:1}
        for num in nums:
            prefix += num
        
            if (prefix - k) in prefix_map:
                count += prefix_map[prefix - k]
            
            if prefix in prefix_map:
                prefix_map[prefix] += 1
            else:
                prefix_map[prefix] = 1
        return count
