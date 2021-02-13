class Solution:
    def rotate(self, nums, k):
        cnt = 1
        length = len(nums)
        k = k % length
        cur_idx = 0
        start = cur_idx
        pre_num = nums[cur_idx]
        while cnt <= length:
            nxt_idx = (cur_idx + k) % length
            tmp = nums[nxt_idx]
            nums[nxt_idx] = pre_num
            pre_num = tmp
            cur_idx = nxt_idx
            cnt += 1
            if start == cur_idx:
                start = (start+1) % length
                cur_idx = start
                pre_num = nums[cur_idx]



class Solution:
    def rotate(self, nums, k):
        def rev(start, end):
            while start < end:
                tmp = nums[end]
                nums[end] = nums[start]
                nums[start] = tmp
                start += 1
                end -= 1
        length = len(nums)
        rev(0, length - 1)
        rev(0, k % length - 1)
        rev(k % length, length - 1)
