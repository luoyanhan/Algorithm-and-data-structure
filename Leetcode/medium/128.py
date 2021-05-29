class Solution:
    def longestConsecutive(self, nums):
        nums_set = set(nums)
        longest = 0
        for num in nums_set:
            if num-1 not in nums_set:
                cur = num
                cur_len = 1
                while cur + 1 in nums_set:
                    cur_len += 1
                    cur += 1
                longest = max(longest, cur_len)
        return longest