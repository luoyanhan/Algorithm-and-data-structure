class Solution:
    def minSetSize(self, arr) -> int:
        import collections
        c_li = collections.Counter(arr).most_common()
        total = len(arr)
        res = 0
        deleted = 0
        for num, c in c_li:
            res += 1
            deleted += c
            if deleted * 2 >= total:
                return res

