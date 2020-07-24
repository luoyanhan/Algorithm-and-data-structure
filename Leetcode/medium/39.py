class Solution:
    def combinationSum(self, candidates, target: int):
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
                path.append(candidates[i])
                dfs(i, new_resident)
                path.pop()

        dfs(0, target)
        return res


