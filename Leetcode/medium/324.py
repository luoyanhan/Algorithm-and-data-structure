class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        length = len(nums)
        nums.sort(reverse=True)
        mid = length//2
        bigger_list = nums[:mid]
        smaller_list = nums[mid:]
        idx = 0
        while bigger_list and idx < length:
            nums[idx] = smaller_list.pop(0)
            nums[idx+1] = bigger_list.pop(0)
            idx += 2
        if smaller_list:
            nums[-1] = smaller_list.pop(0)