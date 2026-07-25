class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:   return 2**31 - 1
        negative = (dividend < 0) ^ (divisor < 0)
        a, b = abs(dividend), abs(divisor)
        ans = 0
        while a >= b:
            temp = b
            count = 1
            while a >= (temp<<1):
                temp <<= 1
                count <<= 1
            ans += count
            a -= temp
        return -ans if negative else ans