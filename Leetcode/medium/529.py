class Solution:
    def updateBoard(self, board, click):
        height = len(board[0])
        width = len(board)
        neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        def cal(i, j):
            res = 0
            for x, y in neighbours:
                 if isLeagle(i+x, j+y) and board[i+x][j+y] == 'M':
                     res += 1
            return res
        def isLeagle(i, j):
            return i >= 0 and i < width and j >= 0 and j < height
        def dfs(i, j):
            num = cal(i, j)
            if num > 0:
                board[i][j] = str(num)
                return
            board[i][j] = 'B'
            for x, y in neighbours:
                 if isLeagle(i+x, j+y) and board[i+x][j+y] == 'E':
                     dfs(i+x, j+y)
        dfs(click[0], click[1])
        return board




