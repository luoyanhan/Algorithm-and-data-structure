class Solution:
    def solveNQueens(self, n: int):
        colum = set()
        diagonal_line_right_top = set()
        diagonal_line_left_top = set()
        Queen = [-1 for _ in range(n)]
        res = list()
        def inner(row):
            if row == n:
                inner_res = list()
                line = ['.' for _ in range(n)]
                for idx in range(n):
                    line[Queen[idx]] = 'Q'
                    inner_res.append(''.join(line))
                    line[Queen[idx]] = '.'
                res.append(inner_res)
            else:
                for col in range(n):
                    if col not in colum \
                        and (row - col) not in diagonal_line_left_top \
                        and (row+col) not in diagonal_line_right_top:
                        colum.add(col)
                        diagonal_line_left_top.add(row-col)
                        diagonal_line_right_top.add(row+col)
                        Queen[row] = col
                        inner(row+1)
                        colum.remove(col)
                        diagonal_line_left_top.remove(row - col)
                        diagonal_line_right_top.remove(row + col)
        inner(0)
        return res

