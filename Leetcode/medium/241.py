class Solution:
    def diffWaysToCompute(self, input: str):
        if input.isdigit():
            return [int(input)]
        res = list()
        for i, c in enumerate(input):
            if c in ['+', '-', '*']:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right:
                        if c == '+':
                            res.append(l + r)
                        elif c == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)
        return res
