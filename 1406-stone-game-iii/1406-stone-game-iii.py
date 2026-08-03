class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            chooseOne = stoneValue[i] - dp[i + 1]
            chooseTwo = stoneValue[i] + stoneValue[i+1] - dp[i + 2] if i < n - 1 else -1000
            chooseThree = stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp[i+3] if i < n - 2 else -1000
            dp[i] = max(chooseOne, chooseTwo, chooseThree)
        if dp[0] == 0:   return "Tie"
        elif dp[0] > 0: return "Alice"
        else:   return "Bob"

