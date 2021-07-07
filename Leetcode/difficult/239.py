import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        q = [(-nums[idx], idx) for idx in range(k)]
        heapq.heapify(q)
        res = list()
        res.append(-q[0][0])
        for idx in range(k, length):
            heapq.heappush(q, (-nums[idx], idx))
            #这里是while而不是if
            while q[0][1] <= idx-k:
                heapq.heappop(q)
            res.append(-q[0][0])
        return res


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = list()
        length = len(nums)
        for idx in range(k):
            while stack and stack[-1][0] < nums[idx]:
                stack.pop()
            stack.append((nums[idx], idx))
        res = [stack[0][0]]
        for idx in range(k, length):
            while stack and stack[-1][0] < nums[idx]:
                stack.pop()
            while stack and stack[0][1] <= idx-k:
                stack.pop(0)
            stack.append((nums[idx], idx))
            res.append((stack[0][0]))
        return res


