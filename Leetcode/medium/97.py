class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        length1, length2, length3 = len(s1), len(s2), len(s3)
        if length1 + length2 != length3:
            return False
        mapper = [[False for j in range(length2+1)] for i in range(length1+1)]
        mapper[0][0] = True
        for i in range(length1+1):
            for j in range(length2+1):
                p = i+j-1
                if i > 0:
                    mapper[i][j] = mapper[i-1][j] and s3[p] == s1[i-1]
                if j > 0:
                    mapper[i][j] = mapper[i][j] or (mapper[i][j-1] and s3[p] == s2[j-1])
        return mapper[length1][length2]


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        length1, length2, length3 = len(s1), len(s2), len(s3)
        if length1 + length2 != length3:
            return False
        mapper = [False for j in range(length2+1)]
        mapper[0] = True
        for i in range(length1+1):
            for j in range(length2+1):
                p = i+j-1
                if i > 0:
                    mapper[j] = mapper[j] and s3[p] == s1[i-1]
                if j > 0:
                    mapper[j] = mapper[j] or (mapper[j-1] and s3[p] == s2[j-1])
        return mapper[length2]


print(Solution().isInterleave('a', '', 'c'))