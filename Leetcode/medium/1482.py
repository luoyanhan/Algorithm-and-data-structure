class Solution:
    def minDays(self, bloomDay, m: int, k: int):
        length = len(bloomDay)
        arr = sorted(set(bloomDay))
        def check(day):
            num = 0
            tmp = 0
            for i in range(length):
                if bloomDay[i] <= day:
                    tmp += 1
                    if tmp >= k:
                        num += 1
                        tmp = 0
                else:
                    tmp = 0
                if num >= m:
                    return True
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if not check(arr[mid]):
                left = mid + 1
            else:
                right = mid
        return arr[left] if check(arr[left]) else -1







print(Solution().minDays([1,10,3,10,2], 3, 2))


