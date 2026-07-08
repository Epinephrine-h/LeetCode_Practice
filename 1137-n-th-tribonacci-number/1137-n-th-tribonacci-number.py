class Solution(object):
    def tribonacci(self, n):
        t0 = 0
        t1 = 1
        t2 = 1
        if n == 0:
            return 0
        if n < 3:
            return 1
        for i in range(3, n + 1):
            cur = t2 + t1 + t0
            t2,t1,t0 = cur, t2, t1
        return t2
        