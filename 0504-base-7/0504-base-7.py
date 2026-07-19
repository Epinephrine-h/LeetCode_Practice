class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        n = abs(num)
        mod = []
        while n:
            x = n % 7
            n //= 7
            mod.append(str(x))
        if num < 0:
            mod.append('-')
        return "".join(mod[::-1])