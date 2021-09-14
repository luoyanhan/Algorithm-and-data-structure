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


import random
class Solution:

    def __init__(self, nums):
        self.nums = nums[:]
        self.cur_nums = nums


    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        self.cur_nums = self.nums[:]
        return self.cur_nums


    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        length = len(self.cur_nums)
        for idx in range(length):
            rand_idx = random.randint(idx, length-1)
            self.cur_nums[idx], self.cur_nums[rand_idx] = self.cur_nums[rand_idx], self.cur_nums[idx]
        return self.cur_nums