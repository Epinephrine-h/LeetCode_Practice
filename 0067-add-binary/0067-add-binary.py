class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        pa, pb, carry = len(a) - 1, len(b) - 1, 0
        while pa >= 0 or pb >= 0 or carry !=0:
            na = 0 if pa < 0 or a[pa] == '0' else 1
            nb = 0 if pb < 0 or b[pb] == '0' else 1
            sum = na + nb + carry
            carry = sum//2
            res.append(str(sum%2))
            pa -= 1
            pb -= 1
        res.reverse()
        return "".join(res)