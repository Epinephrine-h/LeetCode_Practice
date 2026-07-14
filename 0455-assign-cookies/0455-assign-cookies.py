class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j, cnt = len(g) - 1, len(s) - 1, 0
        while i >= 0 and j >= 0:
            if s[j] >= g[i]:
                cnt += 1
                i -= 1
                j -= 1
            else:
                i -= 1
        return cnt