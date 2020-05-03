class Solution:
    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        neighbours = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
        for row in range(rows):
            for col in range(cols):
                live_neighbour = 0
                for i, j in neighbours:
                    new_row = row + i
                    new_col = col + j
                    if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols and \
                            board[new_row][new_col] in [1, -1]:
                        live_neighbour += 1
                if (live_neighbour < 2 or live_neighbour > 3) and board[row][col] == 1:
                    board[row][col] = -1
                elif live_neighbour == 3 and board[row][col] == 0:
                    board[row][col] = 2
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == -1:
                    board[row][col] = 0
                elif board[row][col] == 2:
                    board[row][col] = 1

Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])

