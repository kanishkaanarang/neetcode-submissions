from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Step 1: Count frequency
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        # Step 2: Create buckets
        n = len(nums)
        buckets = []
        for _ in range(n + 1):
            buckets.append([])

        # Step 3: Fill buckets
        for num in freq_map:
            freq = freq_map[num]
            buckets[freq].append(num)

        # Step 4: Collect top k elements
        result = []
        
        # Traverse from highest frequency to lowest
        for i in range(n, -1, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result