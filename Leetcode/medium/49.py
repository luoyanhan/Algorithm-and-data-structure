class Solution:
    def groupAnagrams(self, strs):
        d = dict()
        for each in strs:
            li = list(each)
            li.sort()
            key = ''.join(li)
            if key in d:
                d[key].append(each)
            else:
                d[key] = [each]
        return list(d.values())

print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))