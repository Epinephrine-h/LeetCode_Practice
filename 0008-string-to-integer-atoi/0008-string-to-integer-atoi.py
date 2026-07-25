class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:   return 0
        pointer = ans = 0
        while pointer < len(s) and s[pointer] == ' ':   pointer += 1
        if pointer == len(s):    return 0
        negative = True if s[pointer] == '-' else False
        if s[pointer] == '+' or s[pointer] == '-':    pointer += 1
        while pointer < len(s) and '0' <= s[pointer] <= '9':
            ans = ans * 10 + int(s[pointer])
            pointer += 1
        if negative:
            ans = -ans
            return -2**31 if ans < -2**31 else ans
        return 2**31 - 1 if ans > 2**31 - 1 else ans
