class Solution:
    def alphabetBoardPath(self, target):
        res = ''
        old_x, old_y = 0, 0
        for word in target:
            offset = ord(word) - ord('a')
            x = offset // 5
            y = offset % 5
            if word == 'z':
                res += 'L'*old_y + 'D'*(5-old_x)
            else:
                offset_x = x - old_x
                offset_y = y - old_y
                res += 'U'*(-offset_x) + 'D'*offset_x + 'L'*(-offset_y) + 'R'*offset_y
            old_x = x
            old_y = y
            res += '!'
        return res


