from functools import lru_cache
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @lru_cache
        def recursion(a, b):
            if a < 0 or b < 0 or obstacleGrid[a][b] == 1:
                return 0
            if a == 0 and b == 0:
                return 1
            return recursion(a-1, b) + recursion(a, b-1)
        return recursion(len(obstacleGrid) - 1,len(obstacleGrid[0]) - 1)