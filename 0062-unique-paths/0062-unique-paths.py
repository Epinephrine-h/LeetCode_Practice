from functools import lru_cache 
class Solution(object):
    def uniquePaths(self, m, n):
        @lru_cache(None)
        def recursion(a, b):
            if b < 0 or a < 0:
                return 0
            if a == 0 and b == 0:
                return 1
            
            res = recursion(a - 1, b) + recursion(a, b - 1)
            return res
        return recursion(m - 1, n - 1)