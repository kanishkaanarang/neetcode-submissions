from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        # Step 1: Initialize pointers
        left = 0
        right = len(nums) - 1
        i = 0

        # Step 2: Process array
        while i <= right:

            # Case 1: nums[i] == 0
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1

            # Case 2: nums[i] == 2
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
                # NOTE: don't increment i here

            # Case 3: nums[i] == 1
            else:
                i += 1