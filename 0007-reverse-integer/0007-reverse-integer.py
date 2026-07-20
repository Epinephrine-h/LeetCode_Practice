class Solution:
    def reverse(self, x: int) -> int:
        n, r = abs(x), 0
        while n:
            r = r * 10 + n % 10
            n //= 10
        if -(1 << 31) > r or r > (1 << 31) - 1:
            return 0
        return -r if x < 0 else r