class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for column in range(1,n):   grid[0][column] = grid[0][column-1] + grid[0][column]
        for row in range(1, m):     grid[row][0] = grid[row-1][0] + grid[row][0]
        for row in range(1,m):
            for column in range(1,n):
                grid[row][column] = min(grid[row-1][column], grid[row][column-1]) + grid[row][column]
        return grid[-1][-1]