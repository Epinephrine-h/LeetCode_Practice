class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for column in range(1,n):   dp[0][column] = dp[0][column-1] + grid[0][column]
        for row in range(1, m):     dp[row][0] = dp[row-1][0] + grid[row][0]
        for row in range(1,m):
            for column in range(1,n):
                dp[row][column] = min(dp[row-1][column], dp[row][column-1]) + grid[row][column]
        return dp[-1][-1]