from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        q = deque()  # stores indices
        res = []

        for i in range(len(nums)):
            # remove out-of-window elements
            if q and q[0] < i - k + 1:
                q.popleft()

            # remove smaller elements (they're useless)
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            # start adding results after first window
            if i >= k - 1:
                res.append(nums[q[0]])

        return res