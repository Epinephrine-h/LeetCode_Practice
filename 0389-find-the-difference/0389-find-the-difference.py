class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x, y = sorted(list(s)), sorted(list(t))
        for i in range(len(x)):
            if x[i] != y[i]:
                return y[i]
        return y[-1]