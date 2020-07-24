class Solution:
    def combinationSum2(self, candidates, target: int):
        candidates.sort()
        length = len(candidates)
        path = list()
        res = list()
        def dfs(start, resident):
            if resident == 0:
                res.append(path[:])
                return
            for i in range(start, length):
                new_resident = resident - candidates[i]
                if new_resident < 0:
                    break
                if start < i and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(i+1, new_resident)
                path.pop()

        dfs(0, target)
        return res




