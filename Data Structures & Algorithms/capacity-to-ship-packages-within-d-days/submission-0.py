class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Minimum capacity must be at least the heaviest package
        left = max(weights)

        # Maximum capacity can be sum of all packages
        right = sum(weights)

        result = right

        while left <= right:
            capacity = (left + right) // 2

            days_needed = 1
            current_load = 0

            for weight in weights:
                if current_load + weight > capacity:
                    days_needed += 1
                    current_load = 0

                current_load += weight

            # Capacity works, try smaller
            if days_needed <= days:
                result = capacity
                right = capacity - 1

            # Capacity too small
            else:
                left = capacity + 1

        return result