from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fmap = {}
        for num in nums:
            if num in fmap:
                fmap[num] += 1
            else:
                fmap[num] = 1
        
        n = len(nums)
        buckets = []
        for i in range(n+1):
            buckets.append([])
        
        for num in fmap:
            freq = fmap[num]
            buckets[freq].append(num)
        
        res = []

        for i in range(n,-1,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
                