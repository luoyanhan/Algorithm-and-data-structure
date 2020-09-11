class Solution:
    def restoreIpAddresses(self, s: str):
        res = list()
        segment = [0] * 4
        def inner(segid, segstart):
            if segid == 4:
                if segstart == len(s):
                    res.append('.'.join([str(each) for each in segment]))
                return
            if segstart == len(s):
                return
            if s[segstart] == '0':
                segment[segid] = 0
                inner(segid+1, segstart+1)
            num = 0
            for segend in range(segstart, len(s)):
                num = 10*num + int(s[segend])
                if 0 < num < 256:
                    segment[segid] = num
                    inner(segid+1, segend+1)
                else:
                    break
        inner(0, 0)
        return res
