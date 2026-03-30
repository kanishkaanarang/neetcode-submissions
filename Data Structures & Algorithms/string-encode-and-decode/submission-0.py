from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s

        return result


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # find '#'
            while s[j] != '#':
                j += 1

            # get length
            length = int(s[i:j])

            # get word
            word = s[j + 1 : j + 1 + length]
            result.append(word)

            # move pointer
            i = j + 1 + length

        return result