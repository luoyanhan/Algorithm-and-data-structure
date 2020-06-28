class Solution:
    def asteroidCollision(self, asteroids):
        res = list()
        for i in range(len(asteroids)):
            res.append(asteroids[i])
            while len(res) > 1 and res[-1] < 0 and res[-2] > 0:
                first = res.pop()
                second = res.pop()
                if first + second == 0:
                    break
                res.append(first if abs(first) > abs(second) else second)
        return res

