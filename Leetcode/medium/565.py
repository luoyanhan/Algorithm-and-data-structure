class Solution:
    def arrayNesting(self, nums):
        #visited用数组比用set内存消耗更低,运行时间稍微短一点
        visited = [False for _ in range(len(nums))]
        total = 0
        for num in nums:
            if not visited[num]:
                tmp_total = 0
                idx = num
                while True:
                    tmp_total += 1
                    visited[idx] = True
                    idx = nums[idx]
                    if idx == num:
                        break
                total = max(total, tmp_total)
        return total

