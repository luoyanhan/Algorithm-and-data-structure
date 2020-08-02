class Solution:
    def singleNumber(self, nums):
        one = 0
        two = 0
        for num in nums:
            one = (num ^ one) & ~two
            two = (num ^ two) & ~one
        return one