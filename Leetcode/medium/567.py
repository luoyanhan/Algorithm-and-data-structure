from collections import defaultdict
class Solution:
    def checkInclusion(self, s1, s2):
        mapper1 = defaultdict(int)
        mapper2 = defaultdict(int)
        length1, length2 = len(s1), len(s2)
        if length2 < length1:
            return False
        for i in range(length1):
            mapper1[s1[i]] += 1
            mapper2[s2[i]] += 1
        if mapper1 == mapper2:
            return True
        idx = length1
        while idx < length2:
            mapper2[s2[idx]] += 1
            mapper2[s2[idx-length1]] -= 1
            if mapper2[s2[idx-length1]] == 0:
                del mapper2[s2[idx-length1]]
            if mapper1 == mapper2:
                return True
            idx += 1
        return False

from collections import defaultdict
class Solution:
    def checkInclusion(self, s1, s2):
        mapper = defaultdict(int)
        length1, length2 = len(s1), len(s2)
        if length2 < length1:
            return False
        for i in range(length1):
            mapper[s1[i]] -= 1
            mapper[s2[i]] += 1
        diff = 0
        for each in mapper:
            if mapper[each] != 0:
                diff += 1
        if diff == 0:
            return True
        idx = length1
        while idx < length2:
            if mapper[s2[idx]] == 0:
                diff += 1
            mapper[s2[idx]] += 1
            if mapper[s2[idx]] == 0:
                diff -= 1
            if mapper[s2[idx - length1]] == 0:
                diff += 1
            mapper[s2[idx-length1]] -= 1
            if mapper[s2[idx - length1]] == 0:
                diff -= 1
            if diff == 0:
                return True
            idx += 1
        return False


from collections import defaultdict
class Solution:
    def checkInclusion(self, s1, s2):
        mapper = defaultdict(int)
        length1, length2 = len(s1), len(s2)
        if length2 < length1:
            return False
        for i in range(length1):
            mapper[s1[i]] -= 1
        left = 0
        for right in range(length2):
            mapper[s2[right]] += 1
            while mapper[s2[right]] > 0:
                mapper[s2[left]] -= 1
                left += 1
            if right - left + 1 == length1:
                return True
        return False

print(Solution().checkInclusion("ab", "eidboaoo"))