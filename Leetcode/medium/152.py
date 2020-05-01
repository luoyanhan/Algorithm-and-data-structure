class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        else:
            max_res = nums[0]
            max_p = nums[0]
            min_p = nums[0]
            for i in range(1, length):
                temp = max_p
                max_p = max(max_p*nums[i], nums[i], min_p*nums[i])
                min_p = min(temp*nums[i], nums[i], min_p*nums[i])
                max_res = max(max_p, max_res)
            return max_res

