class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        ans = []
        while i >= 0 or j >= 0 or carry > 0:
            n1 = 0 if i < 0 else int(num1[i])
            n2 = 0 if j < 0 else int(num2[j])
            sum = n1 + n2 + carry
            ans.append(str(sum % 10))
            carry = sum // 10
            i -= 1
            j -= 1
        return "".join(ans[::-1])