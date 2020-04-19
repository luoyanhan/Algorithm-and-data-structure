class Solution:
    def findDuplicate(self, nums) -> int:
        nums.sort()
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        pt1 = slow
        pt2 = nums[0]
        while pt1 != pt2:
            pt1 = nums[pt1]
            pt2 = nums[pt2]
        return pt1



