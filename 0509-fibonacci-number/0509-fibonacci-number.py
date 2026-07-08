class Solution(object):
    def fib(self, n):
        f2 = 0
        f1 = 1
        if n == 0:
            return f2
        for i in range(2,n + 1):
            x = f1 + f2
            f1, f2 = x, f1
        return f1
        