class Solution(object):
    def reverseVowels(self, s):
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        res = list(s)
        left = 0
        right = len(res) - 1
        while left < right:
            while left < right and res[right] not in vowels:
                right -= 1
            while left < right and res[left] not in vowels:
                left += 1
            res[left], res[right] = res[right], res[left]
            left += 1
            right -= 1
        return "".join(res)