class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left = 0

        for right in range(len(nums)):
            # If the window size exceeds k, remove the oldest element
            if right - left > k:
                window.remove(nums[left])
                left += 1
            
            # If the current number is already in the set, we found a duplicate within distance k
            if nums[right] in window:
                return True
            
            # Add the current number to the window
            window.add(nums[right])
            
        return False
