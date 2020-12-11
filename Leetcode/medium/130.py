class Solution:
    def solve(self, board) -> None:
        if not board:
            return
        rows = len(board)
        cols = len(board[0])
        def dfs(board, i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != 'O':
                return
            board[i][j] = '#'
            dfs(board, i - 1, j)
            dfs(board, i + 1, j)
            dfs(board, i, j - 1)
            dfs(board, i, j + 1)
        for i in [0, rows-1]:
            for j in range(cols):
                if board[i][j] == 'O':
                    dfs(board, i, j)
        for i in range(rows):
            for j in [0, cols-1]:
                if board[i][j] == 'O':
                    dfs(board, i, j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'


class Solution:
    def solve(self, board) -> None:
        if not board:
            return
        rows = len(board)
        cols = len(board[0])
        def dfs(i, j):
            nonlocal board
            board[i][j] = '#'
            stack = [[i, j]]
            while stack:
                x, y = stack[-1]
                if 0 <= x+1 < rows and board[x+1][y] == 'O':
                    board[x+1][y] = '#'
                    stack.append([x+1, y])
                    continue
                if 0 <= x-1 < rows and board[x-1][y] == 'O':
                    board[x-1][y] = '#'
                    stack.append([x-1, y])
                    continue
                if 0 <= y+1 < cols and board[x][y+1] == 'O':
                    board[x][y+1] = '#'
                    stack.append([x, y+1])
                    continue
                if 0 <= y-1 < cols and board[x][y-1] == 'O':
                    board[x][y-1] = '#'
                    stack.append([x, y-1])
                    continue
                x, y = stack.pop()
        for i in [0, rows-1]:
            for j in range(cols):
                if board[i][j] == 'O':
                    dfs(i, j)
        for i in range(rows):
            for j in [0, cols-1]:
                if board[i][j] == 'O':
                    dfs(i, j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'


class Solution:
    def solve(self, board) -> None:
        if not board:
            return
        rows = len(board)
        cols = len(board[0])
        def bfs(i, j):
            nonlocal board
            board[i][j] = '#'
            stack = [[i, j]]
            while stack:
                x, y = stack.pop(0)
                if 0 <= x+1 < rows and board[x+1][y] == 'O':
                    board[x+1][y] = '#'
                    stack.append([x+1, y])
                if 0 <= x-1 < rows and board[x-1][y] == 'O':
                    board[x-1][y] = '#'
                    stack.append([x-1, y])
                if 0 <= y+1 < cols and board[x][y+1] == 'O':
                    board[x][y+1] = '#'
                    stack.append([x, y+1])
                if 0 <= y-1 < cols and board[x][y-1] == 'O':
                    board[x][y-1] = '#'
                    stack.append([x, y-1])

        for i in [0, rows-1]:
            for j in range(cols):
                if board[i][j] == 'O':
                    bfs(i, j)
        for i in range(rows):
            for j in [0, cols-1]:
                if board[i][j] == 'O':
                    bfs(i, j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'

