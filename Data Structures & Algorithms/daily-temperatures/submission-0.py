class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []   # stores indices

        for i in range(n):
            # While current temperature is warmer than the temperature
            # at the index on top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                result[prev] = i - prev

            # Push current index
            stack.append(i)

        return result