# The guess API is already defined for you.
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2

            result = guess(mid)

            # Correct guess
            if result == 0:
                return mid

            # Our guess is too high
            elif result == -1:
                right = mid - 1

            # Our guess is too low
            else:
                left = mid + 1