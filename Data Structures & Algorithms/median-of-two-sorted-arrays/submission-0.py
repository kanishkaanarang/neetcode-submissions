class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        # Always binary search on smaller array
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        left = 0
        right = len(A)

        while True:
            i = (left + right) // 2      # Partition in A
            j = half - i                 # Partition in B

            Aleft = A[i - 1] if i > 0 else float('-inf')
            Aright = A[i] if i < len(A) else float('inf')

            Bleft = B[j - 1] if j > 0 else float('-inf')
            Bright = B[j] if j < len(B) else float('inf')

            # Correct partition found
            if Aleft <= Bright and Bleft <= Aright:

                # Odd total length
                if total % 2:
                    return min(Aright, Bright)

                # Even total length
                return (
                    max(Aleft, Bleft) +
                    min(Aright, Bright)
                ) / 2

            # Move left
            elif Aleft > Bright:
                right = i - 1

            # Move right
            else:
                left = i + 1