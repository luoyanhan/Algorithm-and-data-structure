class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        li1 = [int(each) for each in version1.split('.')]
        li2 = [int(each) for each in version2.split('.')]
        length1 = len(li1)
        length2 = len(li2)
        if length1 > length2:
            li2.extend([0]*(length1-length2))
        elif length1 < length2:
            li1.extend([0] * (length2 - length1))
        for i in range(max(length1, length2)):
            if li1[i] > li2[i]:
                return 1
            elif li1[i] < li2[i]:
                return -1
        return 0