class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return '0'
        res = list()
        if (numerator < 0) ^ (denominator < 0):
            res.append('-')
        numerator, denominator = abs(numerator), abs(denominator)
        a, b = divmod(numerator, denominator)
        res.append(str(a))
        if b == 0:
            return ''.join(res)
        res.append('.')
        h = {b: len(res)}
        while b != 0:
            b *= 10
            a, b = divmod(b, denominator)
            res.append(str(a))
            if b in h:
                res.insert(h[b], '(')
                res.append(')')
                break
            h[b] = len(res)
        return ''.join(res)
