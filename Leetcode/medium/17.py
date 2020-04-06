class Solution:
    def letterCombinations(self, digits):
        map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if not digits:
            return []
        result = ['']
        for each in digits:
            for i in range(len(result)):
                pre = result.pop(0)
                for j in map[each]:
                    result.append(pre+j)
        return result

if __name__ == "__main__":
    result = Solution().letterCombinations('23')
    print(result)


