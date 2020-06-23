class Solution:
    def maxArea(self, height) -> int:
        length = len(height)
        i = 0
        j = length - 1
        max_water = 0
        while i < j:
            v = min(height[i], height[j])*(j-i)
            if v > max_water:
                max_water = v
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return max_water
