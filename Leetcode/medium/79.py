class Solution:
    def exist(self, board, word: str) -> bool:
        neighbors = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        rows = len(board)
        cols = len(board[0])
        def search(index, i, j):
            if index == len(word) - 1:
                return board[i][j] == word[index]
            if board[i][j] == word[index]:
                cur = board[i][j]
                board[i][j] = False
                for x, y in neighbors:
                    new_x = i+x
                    new_y = j+y
                    if new_x >= 0 and new_x < rows and new_y >= 0 and new_y < cols and search(index+1, new_x, new_y):
                        return True
                board[i][j] = cur
            return False
        for i in range(rows):
            for j in range(cols):
                if search(0, i, j):
                    return True
        return False



