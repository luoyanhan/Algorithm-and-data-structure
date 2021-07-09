import random
class Solution:

    def __init__(self, nums):
        self.array = nums
        self.original = nums[:]
        self.length = len(self.array)


    def reset(self):
        self.array = self.original[:]
        return self.array


    def shuffle(self):
        for i in range(self.length):
            swap_idx = random.randint(i, self.length-1)
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array
