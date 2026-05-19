class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # Each element: (start_index, height)
        max_area = 0

        for i, h in enumerate(heights):
            start = i

            # Process all bars taller than current bar
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index  # Extend current bar to the left

            stack.append((start, h))

        # Process remaining bars in stack
        n = len(heights)
        for index, height in stack:
            max_area = max(max_area, height * (n - index))

        return max_area