class Solution:
    def countDigitOne(self, n: int) -> int:
        cnt = 0
        p = 1
        while p <= n:
            high = n // (p * 10)
            cur = (n // p) % 10
            low = n % p
            if cur == 1:
                cnt+=high * p + low + 1
            elif cur > 1:
                cnt+=(high + 1) * p
            else:
                cnt+= high * p
            p*=10
        return cnt