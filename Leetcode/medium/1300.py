# class Solution:
#     def findBestValue(self, arr, target):
#         def check_smaller(val):
#             total = 0
#             for each in arr:
#                 total += min(each, val)
#             return total, total <= target
#         def check_bigger(val):
#             total = 0
#             for each in arr:
#                 total += min(each, val)
#             return total, total >= target
#         left_smaller = target // len(arr)
#         right_smaller = max(arr)
#         while left_smaller < right_smaller:
#             mid = (left_smaller + right_smaller + 1) // 2
#             if not check_smaller(mid)[1]:
#                 right_smaller = mid - 1
#             else:
#                 left_smaller = mid
#
#         # left_bigger = target // len(arr)
#         # right_bigger = max(arr)
#         # while left_bigger < right_bigger:
#         #     mid = (left_bigger + right_bigger) // 2
#         #     if not check_bigger(mid)[1]:
#         #         left_bigger = mid + 1
#         #     else:
#         #         right_bigger = mid
#         # if target - check_smaller(right_smaller)[0] <= check_bigger(left_bigger)[0] - target:
#         #     return right_smaller
#         # else:
#         #     return left_bigger
#
#         #right_smaller最接近且不大于 mid，left_bigger最接近且大于 mid, 所以right_smaller <= left_bigger,
#         # 定义left_bigger = right_smaller + 1 再将target - check_smaller(right_smaller)[0] <= check_bigger(left_bigger)[0] - target
#         #改成abs(target - check_smaller(right_smaller)[0]) <= abs(check_bigger(left_bigger)[0] - target)可以节省一次二分查找
#         left_bigger = right_smaller + 1
#         if abs(target - check_smaller(right_smaller)[0]) <= abs(check_bigger(left_bigger)[0] - target):
#             return right_smaller
#         else:
#             return left_bigger


class Solution:
    def findBestValue(self, arr, target):
        arr.sort()
        n = len(arr)
        def get_first_bigger_idx(val):
            left = 0
            right = n-1
            while left < right:
                mid = (left + right) // 2
                if arr[mid] < val:
                    left = mid + 1
                else:
                    right = mid
            return left if arr[left] >= val else -1
        #不用列表分片省一点点内存
        def get_sum(idx):
            total = 0
            for i in range(idx):
                total += arr[i]
            return total
        left = target // n
        right = arr[-1]
        while left < right:
            mid = (left + right + 1) // 2
            idx = get_first_bigger_idx(mid)
            total = get_sum(idx) + mid * (n-idx)
            if total > target:
                right = mid - 1
            else:
                left = mid
        idx_smaller = get_first_bigger_idx(right)
        idx_bigger = get_first_bigger_idx(right + 1)
        total1 = get_sum(idx_smaller) + right * (n - idx_smaller)
        total2 = get_sum(idx_bigger) + (right + 1) * (n - idx_bigger) if idx_bigger != -1 else sum(arr)
        if abs(total1 - target) <= abs(total2 - target):
            return right
        return right + 1


print(Solution().findBestValue( [2,3,5], 11))