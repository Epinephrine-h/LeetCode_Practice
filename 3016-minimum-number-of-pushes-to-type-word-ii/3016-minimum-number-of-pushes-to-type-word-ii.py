from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = Counter(word)
        ans = 0
        for i, fre in enumerate(sorted(cnt.values(), reverse = True)):
            if i < 8:   ans += fre
            elif i < 16:    ans += fre * 2
            elif i < 24:    ans += fre * 3
            else:   ans += fre * 4
        return ans