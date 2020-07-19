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


Solution().solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])




