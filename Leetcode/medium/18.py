class Solution:
    def fourSum(self, nums, target: int):
        nums.sort()
        length = len(nums)
        result = list()
        for i in range(length-3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1, length-2):
                if j > i+1 and nums[j] == nums[j - 1]:
                    continue
                k = j+1
                z = length - 1
                while k < z:
                    temp = nums[i] + nums[j] + nums[k] + nums[z]
                    if temp == target:
                        result.append([nums[i], nums[j], nums[k], nums[z]])
                        while k < z and nums[k+1] == nums[k]:
                            k += 1
                        while k < z and nums[z-1] == nums[z]:
                            z -= 1
                        k += 1
                        z -= 1
                    elif temp > target:
                        z -= 1
                    else:
                        k += 1
        return result

