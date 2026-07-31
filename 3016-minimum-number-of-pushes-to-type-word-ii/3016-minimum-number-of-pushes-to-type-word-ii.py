from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = Counter(word)
        return sum(fre * (i // 8 + 1) for i, fre in enumerate(sorted(cnt.values(), reverse = True)))