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
                if offset_x < 0:
                    res += 'U'*abs(offset_x)
                else:
                    res += 'D'*abs(offset_x)
                if offset_y < 0:
                    res += 'L'*abs(offset_y)
                else:
                    res += 'R'*abs(offset_y)
            old_x = x
            old_y = y
            res += '!'
        return res


