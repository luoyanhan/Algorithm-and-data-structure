class Solution:
    def totalNQueens(self, n: int) -> int:
        colum = set()
        left_down = set()
        right_down = set()
        res = 0
        def inner(row):
            nonlocal res
            if row == n:
                res += 1
            else:
                for col in range(n):
                    if col not in colum and (row+col) not in left_down and (col-row) not in right_down:
                        colum.add(col)
                        left_down.add(row+col)
                        right_down.add(col-row)
                        inner(row+1)
                        colum.remove(col)
                        left_down.remove(row + col)
                        right_down.remove(col - row)
        inner(0)
        return res