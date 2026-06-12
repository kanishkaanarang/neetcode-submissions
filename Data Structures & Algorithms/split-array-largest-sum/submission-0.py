class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        left = max(nums)
        right = sum(nums)

        while left <= right:

            mid = (left + right) // 2

            count = 1
            currSum = 0

            for num in nums:

                if currSum + num > mid:
                    count += 1
                    currSum = num
                else:
                    currSum += num

            if count <= k:
                right = mid - 1
            else:
                left = mid + 1

        return left