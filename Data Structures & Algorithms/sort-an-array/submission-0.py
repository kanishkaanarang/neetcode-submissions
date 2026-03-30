from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # Step 1: Base case
        if len(nums) <= 1:
            return nums

        # Step 2: Split array into halves
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        # Step 3: Recursively sort both halves
        left_sorted = self.sortArray(left)
        right_sorted = self.sortArray(right)

        # Step 4: Merge sorted halves
        return self.merge(left_sorted, right_sorted)

    def merge(self, left, right):
        result = []
        i = 0
        j = 0

        # Step 5: Compare elements and merge
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Step 6: Add remaining elements
        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result