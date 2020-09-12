class Solution:
    def minCost(self, s: str, cost) -> int:
        length = len(cost)
        ptr = 0
        res = 0
        while ptr < length-1:
            if s[ptr] != s[ptr+1]:
                ptr += 1
            else:
                max = cost[ptr]
                res += cost[ptr]
                while ptr < length-1 and s[ptr] == s[ptr+1]:
                    res += cost[ptr+1]
                    if cost[ptr+1] > max:
                        max = cost[ptr+1]
                    ptr += 1
                res -= max
        return res

print(Solution().minCost("aabaa", [1,2,3,4,1]))