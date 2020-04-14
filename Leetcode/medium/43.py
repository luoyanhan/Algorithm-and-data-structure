class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        li1 = num1.split()
        li2 = num2.split()
        res = 0
        for i in range(1, len(li1)+1):
            cur = int(li1[-i])*(10**(i-1))
            for j in range(1, len(li2)+1):
                cur2 = int(li2[-j])*(10**(j-1))
                res += cur*cur2
        return str(res)


