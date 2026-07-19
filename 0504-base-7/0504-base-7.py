class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        sign = '-' if num < 0 else ''
        num = -num if num < 0 else num
        mod = []
        while num:
            x = num % 7
            num //= 7
            mod.append(str(x))
        mod.append(sign)
        return "".join(mod[::-1])