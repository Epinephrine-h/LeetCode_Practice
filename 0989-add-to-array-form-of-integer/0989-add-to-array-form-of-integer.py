class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i, carry = len(num) - 1, 0
        ans = []
        while i >= 0 or k >0 or carry > 0:
            num1 = 0 if i < 0 else num[i]
            num2 = 0 if not k else k % 10
            k //= 10
            sum = num1 + num2 + carry
            ans.append(sum%10)
            carry = sum // 10
            i -= 1
        return ans[::-1]