from collections import deque
class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = deque()
        self.length = 0
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if self.length < self.maxSize:
            self.stack.append(x)
            self.length += 1


    def pop(self) -> int:
        if not self.stack:
            return -1
        self.length -= 1
        return self.stack.pop()


    def increment(self, k: int, val: int) -> None:
        idx = 0
        while idx < k and idx < self.length:
            self.stack[idx] += val
            idx += 1


class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [0 for _ in range(maxSize)]
        self.incre = [0 for _ in range(maxSize)]
        self.top = -1
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if self.top < self.maxSize-1:
            self.top += 1
            self.stack[self.top] = x


    def pop(self) -> int:
        if self.top < 0:
            return -1
        res = self.stack[self.top] + self.incre[self.top]
        self.stack[self.top] = 0
        if self.top > 0:
            self.incre[self.top-1] += self.incre[self.top]
        self.incre[self.top] = 0
        self.top -= 1
        return res


    def increment(self, k: int, val: int) -> None:
        idx = min(self.top, k-1)
        if idx >= 0:
            self.incre[idx] += val



# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)