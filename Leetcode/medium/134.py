class Solution:
    def canCompleteCircuit(self, gas, cost):
        length = len(gas)
        start = 0
        while start < length:
            sum_gas = 0
            sum_cost = 0
            cnt = 0
            while cnt < length:
                idx = (start + cnt) % length
                sum_gas += gas[idx]
                sum_cost += cost[idx]
                if sum_cost > sum_gas:
                    break
                cnt += 1
            if cnt == length:
                return start
            start = start + cnt + 1
        return -1
