class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        N = len(nums)
        dp = [[0] * N for _ in range(N)]
        for i in range(N):  dp[i][i] = nums[i]
        for length in range(2, N + 1):
            for i in range(N - length + 1):
                j = i + length - 1
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j-1])
        return dp[0][N - 1] >= 0