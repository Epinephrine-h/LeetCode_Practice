class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        ans = []
        com = max(candies)
        for i in range(len(candies)):
            tmp = candies[i] + extraCandies
            if tmp < com:
                ans.append(False)
            else:
                ans.append(True)
        return ans
        