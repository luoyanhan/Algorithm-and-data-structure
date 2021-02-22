class Solution:
    def countBattleships(self, board):
        row = len(board)
        col = len(board[0])
        cnt = 0
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'X' and (i == 0 or board[i-1][j] == '.') and (j==0 or board[i][j-1] == '.'):
                    cnt += 1
        return cnt