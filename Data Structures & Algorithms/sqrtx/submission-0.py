class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = 1
        right = x

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            # Perfect square
            if square == x:
                return mid

            # Square is too small
            elif square < x:
                left = mid + 1

            # Square is too large
            else:
                right = mid - 1

        # right will be the floor value of sqrt(x)
        return right