class Solution(object):
    def climbStairs(self, n):
        pre1 = 1
        pre2 = 1
        for i in range(2, n + 1):
            cur = pre1 + pre2
            pre1, pre2 = cur, pre1
        return pre1
        