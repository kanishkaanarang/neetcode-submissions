class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Target is in the right half
            elif nums[mid] < target:
                left = mid + 1

            # Target is in the left half
            else:
                right = mid - 1

        # Target not found
        return -1