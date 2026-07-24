class Solution:
    def longestPalindrome(self, s: str) -> str:
        def help(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        res = ""
        for i in range(len(s)):
            test = help(i,i)
            if len(test) > len(res):    res = test
            test = help(i,i+1)
            if len(test) > len(res):    res = test
        return res