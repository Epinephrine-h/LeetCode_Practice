class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        origin = x
        tmp = 0
        while x:
            tmp = tmp * 10 + x % 10
            x //= 10
        return tmp == origin