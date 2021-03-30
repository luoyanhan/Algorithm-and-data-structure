class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        nums = list()
        for word in num:
            while k and nums and nums[-1] > word:
                nums.pop()
                k -= 1
            nums.append(word)
        nums = nums[:-k] if k > 0 else nums
        return str(int(''.join(nums))) if nums else '0'


print(Solution().removeKdigits('10', 2))