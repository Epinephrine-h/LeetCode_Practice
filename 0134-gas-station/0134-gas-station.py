class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        total_gas = 0
        car_tank = 0
        for i in range(len(gas)):
            supply = gas[i] - cost[i]
            total_gas += supply
            car_tank += supply
            if car_tank < 0:
                start = i + 1
                car_tank = 0
        if total_gas < 0:
            return -1
        return start