from collections import deque
class MaxQueue:

    def __init__(self):
        self.indices = deque()
        self.enteties = deque()


    def max_value(self) -> int:
        if not self.indices:
            return -1
        return self.indices[0]


    def push_back(self, value: int) -> None:
        self.enteties.append(value)
        while self.indices and self.indices[-1] < value:
            self.indices.pop()
        self.indices.append(value)



    def pop_front(self) -> int:
        if not self.enteties:
            return -1
        value = self.enteties.popleft()
        if value == self.indices[0]:
            self.indices.popleft()
        return value



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()