class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        bucket = dict()
        length = len(nums)
        for i in range(length):
            bucket_no = nums[i] // (t+1)
            if bucket_no in bucket:
                return True
            elif bucket_no + 1 in bucket and abs(bucket[bucket_no+1]-nums[i]) <= t:
                return True
            elif bucket_no - 1 in bucket and abs(bucket[bucket_no-1]-nums[i]) <= t:
                return True
            bucket[bucket_no] = nums[i]
            if i >= k:
                del bucket[nums[i-k] // (t+1)]
        return False


print(Solution().containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))