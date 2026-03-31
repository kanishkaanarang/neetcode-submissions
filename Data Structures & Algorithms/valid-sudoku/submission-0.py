from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = set()
        cols = set()
        boxes = set()

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                # box index
                box = (r // 3, c // 3)

                # check duplicates
                if (r, val) in rows:
                    return False
                if (c, val) in cols:
                    return False
                if (box, val) in boxes:
                    return False

                # add to sets
                rows.add((r, val))
                cols.add((c, val))
                boxes.add((box, val))

        return True