class Solution(object):
    def maxProfit(self, prices):
        ans = 0
        buy = float('inf')
        for i in range(len(prices)):
            if ans < prices[i] - buy:
                ans = prices[i] - buy
            if buy > prices[i]:
                buy = prices[i]
        return ans
        