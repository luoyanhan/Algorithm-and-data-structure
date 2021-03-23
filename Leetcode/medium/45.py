#顺着来
class Solution:
    def jump(self, nums: List[int]) -> int:
        max_pos = 0
        step = 0
        end = 0
        length = len(nums)
        for i in range(length-1):
            if max_pos >= i:
                max_pos = max(max_pos, i+nums[i])
                if i == end:
                    end = max_pos
                    step += 1
        return step

#倒着来
class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        pos = length - 1
        step = 0
        while pos > 0:
            for i in range(pos):
                if i + nums[i] >= pos:
                    pos = i
                    step += 1
                    break
        return step
