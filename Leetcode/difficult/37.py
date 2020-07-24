class Solution:
    def solveSudoku(self, board):
        box_index = lambda row, col: (row // n) * n + col // n

        def could_place(num, x, y):
            return not (num in rows[x] or num in columns[y] or num in boxes[box_index(x, y)])

        def place(num, x, y):
            rows[x][num] += 1
            columns[y][num] += 1
            boxes[box_index(x, y)][num] += 1
            board[x][y] = str(num)

        def remove_num(num, x, y):
            del rows[x][num]
            del columns[y][num]
            del boxes[box_index(x, y)][num]
            board[x][y] = '.'

        def place_next_number(x, y):
            if x == N-1 and y == N-1:
                nonlocal sloved
                sloved = True
            else:
                if y == N-1:
                    backtrace(x+1, 0)
                else:
                    backtrace(x, y+1)

        def backtrace(x, y):
            if board[x][y] == '.':
                for num in range(1, 10):
                    if could_place(num, x, y):
                        place(num, x, y)
                        place_next_number(x, y)
                        if not sloved:
                            remove_num(num, x, y)
            else:
                place_next_number(x, y)

        from collections import defaultdict
        n = 3
        N = n * n
        rows = [defaultdict(int) for i in range(N)]
        columns = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    place(d, i, j)
        sloved = False
        backtrace(0, 0)

class Solution:   #mine rewrite
    def solveSudoku(self, board):
        n = 3
        rows = [[False]*(n*n+1) for i in range(n*n)]
        cols = [[False]*(n*n+1) for i in range(n*n)]
        boxes = [[False]*(n*n+1) for i in range(n*n)]
        flag = False

        def get_box_index(x, y):
            return x//n*n + y//n

        def place(num, x, y):
            rows[x][num] = True
            cols[y][num] = True
            boxes[get_box_index(x, y)][num] = True
            board[x][y] = str(num)

        def remove(num, x, y):
            rows[x][num] = False
            cols[y][num] = False
            boxes[get_box_index(x, y)][num] = False
            board[x][y] = '.'

        def could_place(num, x, y):
            return not rows[x][num] and not cols[y][num] and not boxes[get_box_index(x, y)][num]

        def backtrack(x, y):
            if board[x][y] == '.':
                for num in range(1, 10):
                    if could_place(num, x, y):
                        place(num, x, y)
                        judge_next(x, y)
                        if not flag:
                            remove(num, x, y)
            else:
                judge_next(x, y)

        def judge_next(x, y):
            if x == n*n-1 and y == n*n-1:
                nonlocal flag
                flag = True
            else:
                if y == n*n-1:
                    backtrack(x+1, 0)
                else:
                    backtrack(x, y+1)

        for x in range(n*n):
            for y in range(n*n):
                if board[x][y] != '.':
                    place(int(board[x][y]), x, y)
        backtrack(0, 0)


Solution().solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])




