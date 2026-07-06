class Solution(object):
    def longestCommonPrefix(self, strs):
        ans = strs[0]
        for i in strs:
            n = min(len(ans), len(i))
            ans = ans[:n]
            for j in range(n - 1, -1, -1):
                if ans[j] != i[j]:
                    ans = ans[:j]
        return "".join(ans)
        