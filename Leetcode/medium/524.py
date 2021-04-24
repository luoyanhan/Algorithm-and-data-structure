class Solution:
    def findLongestWord(self, s, dictionary):
        length = len(s)
        def can_build(s, child):
            idx = 0
            for each in child:
                while s[idx] != each and idx < length:
                    idx += 1
                if idx > length - 1:
                    return False
                idx += 1
            return True