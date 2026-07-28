from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = Counter(s)
        ans = []
        mid = ""
        for ch in sorted(cnt.keys()):
            if cnt[ch] % 2 == 1:    mid = ch
            for _ in range(cnt[ch]//2):  ans.append(ch)
        left = "".join(ans)
        return left + mid + left[::-1]