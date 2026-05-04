class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in mapping:  # closing bracket
                if not stack or stack[-1] != mapping[c]:
                    return False
                stack.pop()
            else:  # opening bracket
                stack.append(c)

        return len(stack) == 0