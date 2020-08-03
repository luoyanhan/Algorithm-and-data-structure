class Solution:
    def singleNumber(self, nums):
        bitmask = 0
        for num in nums:
            bitmask ^= num
        a = b = bitmask
        mask = 1
        while not mask & bitmask:
            mask <<= 1
        for num in nums:
            if num & mask:
                a ^= num
            else:
                b ^= num
        return [a, b]
