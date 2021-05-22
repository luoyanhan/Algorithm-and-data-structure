class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val


    def sumRange(self, left: int, right: int) -> int:
        total = 0
        for idx in range(left, right+1):
            total += self.nums[idx]
        return total


import math
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        length_nums = len(nums)
        l = math.sqrt(length_nums)
        self.length = int(math.ceil(length_nums/l))
        self.b = [0 for _ in range(self.length)]
        for i in range(length_nums):
            self.b[int(i/self.length)] += nums[i]

    def update(self, index: int, val: int) -> None:
        self.b[int(index/self.length)] += val-self.nums[index]
        self.nums[index] = val


    def sumRange(self, left: int, right: int) -> int:
        total = 0
        start_block = int(left/self.length)
        end_block = int(right/self.length)
        if start_block == end_block:
            for i in range(left, right+1):
                total += self.nums[i]
        else:
            for i in range(left, (start_block+1)*self.length):
                total += self.nums[i]
            for i in range(start_block+1, end_block):
                total += self.b[i]
            for i in range(end_block*self.length, right+1):
                total += self.nums[i]
        return total
