class Solution:
    def singleNumber(self, nums):
        one = 0
        two = 0
        for num in nums:
            one = (num ^ one) & ~two
            two = (num ^ two) & ~one
        return one


class Solution:
    def singleNumber(self, nums):
        one = 0
        two = 0
        for num in nums:
            two |= num & one
            one = one ^ num
            three = one & two
            one = one & ~three
            two = two & ~three
        return one
