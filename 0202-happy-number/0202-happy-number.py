class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            tmp = 0
            while n:
                digit = n % 10
                tmp += digit * digit
                n = n // 10
            n = tmp
        return n == 1
