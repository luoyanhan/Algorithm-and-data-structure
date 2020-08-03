class Solution:
    def numSplits(self, s):
        from collections import defaultdict
        count_r = defaultdict(int)
        count_l = defaultdict(int)
        ans = 0
        for each in s:
            count_r[each] += 1
        for each in s:
            count_l[each] += 1
            count_r[each] -= 1
            if count_r[each] == 0:
                del count_r[each]
            if len(count_l.keys()) == len(count_r.keys()):
                ans += 1
        return ans

