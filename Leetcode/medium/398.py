import random
class Solution:

    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        res = None
        suit_idx = 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                if random.randint(0, suit_idx) == 0:
                    res = i
                suit_idx += 1
        return res



print(Solution([1,2,3,3,3]).pick(3))
