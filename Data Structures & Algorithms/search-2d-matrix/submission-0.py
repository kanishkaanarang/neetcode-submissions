class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = (left + right) // 2

            # Convert 1D index to 2D index
            row = mid // cols
            col = mid % cols

            value = matrix[row][col]

            # Target found
            if value == target:
                return True

            # Search right half
            elif value < target:
                left = mid + 1

            # Search left half
            else:
                right = mid - 1

        return False