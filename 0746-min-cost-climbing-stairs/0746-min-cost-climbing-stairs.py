class Solution(object):
    def minCostClimbingStairs(self, cost):
        f2 = 0
        f1 = 0
        for i in range(2, len(cost) + 1):
            cur = min(f1 + cost[i-1],f2 + cost[i-2])
            f1, f2 = cur, f1
        return f1
        