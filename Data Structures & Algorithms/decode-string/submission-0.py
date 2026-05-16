class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        curr_num = 0

        for ch in s:
            # Build the number (handles multi-digit numbers like 12[a])
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)

            # Start of a new encoded block
            elif ch == '[':
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0

            # End of current block
            elif ch == ']':
                prev_str, num = stack.pop()
                curr_str = prev_str + curr_str * num

            # Regular character
            else:
                curr_str += ch

        return curr_str