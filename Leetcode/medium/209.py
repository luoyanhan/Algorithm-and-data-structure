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
        for i in range(1, length):
            nums[i] += nums[i-1]
        left = 0
        right = length - 1
        while right >= left:
            mid = (left + right)//2
        return min_length if min_length < float('inf') else 0