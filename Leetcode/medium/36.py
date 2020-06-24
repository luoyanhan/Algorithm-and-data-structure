class Solution:
    def isValidSudoku(self, board) -> bool:
        rows = [{} for i in range(9)]
        cols = [{} for j in range(9)]
        boxes = [{} for k in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    box_index = i // 3 * 3 + j // 3
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                    rows[i][num] = rows[i].get(num, 0) + 1
                    cols[j][num] = cols[j].get(num, 0) + 1
                    if boxes[box_index][num] > 1 or rows[i][num] > 1 or cols[j][num] > 1:
                        return False
        return True




