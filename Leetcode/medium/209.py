class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        length = len(nums)
        min_length = float('inf')
        for i in range(length):
            total = 0
            for j in range(i, length):
                total += nums[j]
                if total >= s:
                    min_length = min(min_length, j-i+1)
                    break
        return min_length if min_length != float('inf') else 0




class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        length = len(nums)
        min_length = float('inf')
        pre = next = 0
        total = 0
        while next < length:
            total += nums[next]
            while total >= s:
                min_length = min(min_length, next - pre + 1)
                total -= nums[pre]
                pre += 1
            next += 1
        return min_length if min_length < float('inf') else 0



class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        length = len(nums)
        min_length = float('inf')
        pre_sum = [0]
        for i in range(length):
            pre_sum.append(pre_sum[-1] + nums[i])
        def binary(left, right, target):
            while left < right:
                mid = (left+right) // 2
                if target > pre_sum[mid]:
                    left = mid + 1
                else:
                    right = mid
            return left if pre_sum[left] >= target else -1
        for i in range(length+1):
            target = s + pre_sum[i]
            left = i
            right = length
            res = binary(left, right, target)
            if res == -1:
                continue
            min_length = min(min_length, res-i)
        return min_length if min_length < float('inf') else 0


print(Solution().minSubArrayLen(15, [1,2,3,4,5]))

