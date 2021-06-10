class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        length = len(num)
        if length < 3:
            return False

        def check(part1, part2, j):
            while j < length:
                p = str(int(part1) + int(part2))
                if p != num[j:j+len(p)]:
                    return False
                j += len(p)
                part1, part2 = part2, p
            return True

        for i in range(1, length//2 + 1) if num[0] != '0' else [1]:
            for j in range(i+1, length) if num[i] != '0' else [i+1]:
                part1 = num[:i]
                part2 = num[i:j]
                if check(part1, part2, j):
                    return True
        return False

