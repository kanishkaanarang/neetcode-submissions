class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        # Split path by '/'
        for part in path.split('/'):

            # Ignore empty parts and current directory "."
            if part == '' or part == '.':
                continue

            # Go to parent directory if possible
            elif part == '..':
                if stack:
                    stack.pop()

            # Valid directory name
            else:
                stack.append(part)

        # Join all directories with '/'
        return '/' + '/'.join(stack)