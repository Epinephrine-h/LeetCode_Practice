from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = Counter(s)
        tmp = list(cnt.keys())
        tmp.sort()
        ans = []
        mid = None
        for ch in tmp:
            if cnt[ch] % 2 == 1:
                mid = ch
            for _ in range(cnt[ch]//2):  ans.append(ch)
        if mid: return "".join(ans) + str(mid) + "".join(ans[::-1])
        return "".join(ans) + "".join(ans[::-1])