class Solution(object):
    def maxProfit(self, prices):
        ans = 0
        buy = float('inf')
        for i in range(len(prices)):
            ans = max(ans, prices[i] - buy)
            buy = min(buy, prices[i])
        return ans
        