class Solution:
    def findRepeatedDnaSequences(self, s: str):
        res = set()
        map = set()
        length = len(s)
        for i in range(length-10+1):
            child = s[i:i+10]
            if child in map:
                res.add(child)
            else:
                map.add(child)
        return list(res)


class Solution:
    def findRepeatedDnaSequences(self, s: str):
        res = set()
        visited = set()
        length = len(s)
        p = pow(4, 10)
        mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        nums = [mapping[key] for key in s]
        target = 0
        for i in range(length-10+1):
            if i > 0:
                target = target*4 - nums[i-1]*p + nums[i+10-1]
            else:
                for j in range(10):
                    target = target*4 + nums[j]
            if target in visited:
                res.add(s[i:i+10])
            else:
                visited.add(target)
        return list(res)


