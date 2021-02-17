class Solution:
    def majorityElement(self, nums):
        num1 = None
        vote1 = 0
        num2 = None
        vote2 = 0
        total = 0
        for num in nums:
            total += 1
            if num1 == num:
                vote1 += 1
                continue
            if num2 == num:
                vote2 += 1
                continue
            if vote1 == 0:
                num1 = num
                vote1 += 1
                continue
            if vote2 == 0:
                num2 = num
                vote2 += 1
                continue
            vote1 -= 1
            vote2 -= 1
        cnt1 = 0
        cnt2 = 0
        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
        res = list()
        if cnt1 > total // 3:
            res.append(num1)
        if cnt2 > total // 3:
            res.append(num2)
        return res