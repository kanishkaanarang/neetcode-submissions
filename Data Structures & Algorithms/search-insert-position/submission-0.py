class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Search right half
            elif nums[mid] < target:
                left = mid + 1

            # Search left half
            else:
                right = mid - 1

        # Position where target should be inserted
        return left