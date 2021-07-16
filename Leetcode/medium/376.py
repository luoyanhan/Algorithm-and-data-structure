class Solution:
    def wiggleMaxLength(self, nums):
        length = len(nums)
        if length < 2:
            return length
        up = [1] + [0 for _ in range(length-1)]
        down = [1] + [0 for _ in range(length - 1)]
        for idx in range(1, length):
            if nums[idx] - nums[idx-1] > 0:
                up[idx] = down[idx-1] + 1
                down[idx] = down[idx-1]
            elif nums[idx] - nums[idx-1] < 0:
                down[idx] = up[idx - 1] + 1
                up[idx] = up[idx - 1]
            else:
                down[idx] = down[idx - 1]
                up[idx] = up[idx - 1]
        return max(up[-1], down[-1])

class Solution:
    def wiggleMaxLength(self, nums):
        length = len(nums)
        if length < 2:
            return length
        up = 1
        down = 1
        for idx in range(1, length):
            if nums[idx] - nums[idx-1] > 0:
                up = down + 1
            elif nums[idx] - nums[idx-1] < 0:
                down = up + 1
        return max(up, down)


class Solution:
    def wiggleMaxLength(self, nums):
        length = len(nums)
        if length < 2:
            return length
        pre_diff = nums[1] - nums[0]
        res = 2 if pre_diff else 1
        for i in range(2, length):
            cur_diff = nums[i] - nums[i-1]
            if (pre_diff <= 0 and cur_diff > 0) or (pre_diff >= 0 and cur_diff < 0):
                res += 1
                pre_diff = cur_diff
        return res



print(Solution().wiggleMaxLength([1, 1]))