from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        hasOdd = False
        res = 0
        for count in counts.values():
            res += count // 2 * 2
            if count % 2 == 1:
                hasOdd = True
        return res + 1 if hasOdd else res