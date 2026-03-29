from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # sudoku is valid if:
        # each row contains 1-9 without duplicates - set
        # each column contains 1-9 without duplicates
        # each of 3x3 sub-boxes (9 of them) must contain 1-9 without duplicates

        # use buckets?
        rows = [set () for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue
                
                # check if already in any of the buckets
                if (val in rows[r] or
                    val in cols[c] or
                    val in boxes[(r // 3, c //3)]):
                    return False

                # place into three buckets
                rows[r].add(val) 
                cols[c].add(val)
                boxes[(r // 3, c // 3)].add(val)
        return True
                    