class Solution:
    def maxProduct(self, n: int) -> int:
        max_digit, max2_digit = -1, -1
        while n:
            digit = n % 10
            if digit >= max_digit:
                max2_digit = max_digit
                max_digit = digit
            elif digit >= max2_digit:
                max2_digit = digit
            n = n // 10
        return max_digit * max2_digit