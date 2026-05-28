class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        result = right

        while left <= right:
            k = (left + right) // 2

            # Calculate total hours needed at speed k
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k   # Ceiling division

            # Can finish within h hours
            if hours <= h:
                result = k
                right = k - 1

            # Need faster speed
            else:
                left = k + 1

        return result