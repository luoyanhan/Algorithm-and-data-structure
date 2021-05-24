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


class NumArray:

    def __init__(self, nums: List[int]):
        self.length = len(nums)
        self.tree = [0 for _ in range(2*self.length)]
        for i in range(self.length, 2*self.length):
            self.tree[i] = nums[i-self.length]
        for i in range(self.length-1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]



    def update(self, index: int, val: int) -> None:
        index += self.length
        self.tree[index] = val
        while index > 0:
            if index % 2 == 0:
                left = index
                right = index + 1
            else:
                left = index - 1
                right = index
            self.tree[left//2] = self.tree[left] + self.tree[right]
            index = index // 2



    def sumRange(self, left: int, right: int) -> int:
        left += self.length
        right += self.length
        total = 0
        while left <= right:
            if left % 2 == 1:
                total += self.tree[left]
                left += 1
            if right % 2 == 0:
                total += self.tree[right]
                right -= 1
            left = left // 2
            right = right // 2
        return total
