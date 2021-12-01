class Solution:
    def convert(self, s, numRows):
        length = len(s)
        if numRows == 1 or not s:
            return s
        left = length % (2*numRows-2)
        temp_x = int(length/(2*numRows-2))*(numRows-1)
        if left == 0:
            x = temp_x
        else:
            if left <= numRows:
                x = temp_x + 1
            elif left <= (2*numRows-1):
                x = temp_x + left - numRows + 1
            else:
                x = temp_x + numRows
        matrix = []
        for i in range(numRows):
            matrix.append([0 for i in range(x)])
        for i in range(len(s)):
            each = s[i]
            index = i + 1
            x, y = self.locate(index, numRows)
            matrix[y][x] = each
        result = ''.join([matrix[i][j] for i in range(numRows) for j in range(x+1) if matrix[i][j]])
        return result

    def locate(self, index, numRows):
        x1 = int(index/(2*numRows-2))*(numRows-1)-1
        left = index % (2*numRows-2)
        if left == 0:
            x = x1
            y = 1
        else:
            if left <= numRows:
                x = x1 + 1
                y = left - 1
            elif left <= (2*numRows-1):
                x = x1 + left - numRows + 1
                y = 2*numRows - 1 - left
            else:
                x = x1 + numRows
                y = left - 2*numRows
        return (x, y)


class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        rows = ['' for _ in range(numRows)]
        row_idx = 0
        direction = -1
        for word in s:
            rows[row_idx] += word
            if direction < 0:
                row_idx += 1
                if row_idx >= numRows:
                    direction = 1
                    row_idx -= 2
            else:
                row_idx -= 1
                if row_idx < 0:
                    direction = -1
                    row_idx += 2
        return ''.join(rows)



if __name__ == "__main__":
    s = Solution()
    print(s.convert('A', 1))