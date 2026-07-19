class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        idx = s.find('6')
        return num if idx == -1 else int(s[:idx] + '9' + s[idx + 1:])