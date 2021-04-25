class Solution:
    def findLongestWord(self, s, dictionary):
        def is_subseq(word):
            idx = 0
            l = len(word)
            for each in s:
                if each == word[idx]:
                    idx += 1
                if idx >= l:
                    break
            return idx == len(word)
        dictionary.sort(key=lambda x: (-len(x), x))
        for each in dictionary:
            if is_subseq(each):
                return each
        return ''


class Solution:
    def findLongestWord(self, s, dictionary):
        def is_subseq(word):
            idx = 0
            l = len(word)
            for each in s:
                if each == word[idx]:
                    idx += 1
                if idx >= l:
                    break
            return idx == len(word)
        res = ''
        for each in dictionary:
            if is_subseq(each) and len(each) >= len(res):
                if len(each) > len(res):
                    res = each
                elif each < res:
                    res = each
        return res



print(Solution().findLongestWord("abpcplea", ["a","b","c"]))