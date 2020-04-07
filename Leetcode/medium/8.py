class Solution:
    def myAtoi(self, str: str) -> int:
        S = str.strip()
        result = S
        for i in range(len(S)):
            if not S[i].isdigit() and S[i] not in ['+', '-']:
                result = ''.join(S[:i])
                break
        if not result or (result[0] in ['+', '-'] and len(result) == 1) or \
                (result[0] in ['+', '-'] and result[1] in ['+', '-']):
            return 0
        first = ''
        if result[0] in ['+', '-']:
            first = result[0]
        temp = result.replace('+', ' ').replace('-', ' ')
        temp_li = temp.split()
        result = 0
        for each in temp_li:
            if each:
                result = int(first + each)
                break
        if result < -2**31:
            return -2**31
        elif result > 2**31-1:
            return 2**31-1
        else:
            return result
