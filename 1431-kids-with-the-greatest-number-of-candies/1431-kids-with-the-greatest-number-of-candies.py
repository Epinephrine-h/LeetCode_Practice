class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        ans = []
        for i in range(len(candies)):
            tmp = candies[i] + extraCandies
            ok = True
            for j in range(len(candies)):
                if tmp < candies[j]:
                    ok = False

            ans.append(ok)
        return ans
        