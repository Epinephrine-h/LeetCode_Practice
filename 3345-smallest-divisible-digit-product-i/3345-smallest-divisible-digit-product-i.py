class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for num in range(n, 101):
            tmp = num
            product = 1
            while tmp:
                product *= (tmp % 10)
                tmp //= 10
            if product % t == 0:    return num