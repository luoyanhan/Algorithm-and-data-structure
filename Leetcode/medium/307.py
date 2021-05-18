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



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)