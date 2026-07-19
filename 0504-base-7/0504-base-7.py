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
        mod.append('-' if num < 0 else '')
        return "".join(mod[::-1])