class Solution(object):
    def pivotInteger(self, n):
        total = sum(i for i in range(1, n + 1))
        left = 0
        for i in range(1, n + 1):
            left += i
            if left == total - left + i:
                return i
        return -1
        