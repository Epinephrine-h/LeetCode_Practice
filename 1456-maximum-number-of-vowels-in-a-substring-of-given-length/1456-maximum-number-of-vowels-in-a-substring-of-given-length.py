class Solution(object):
    def maxVowels(self, s, k):
        vowels = ['a', 'e', 'i', 'o', 'u']
        cnt = 0
        for i in range(k):
            if s[i] in vowels:
                cnt += 1
        res_max = cnt
        for i in range(k, len(s)):
            if s[i] in vowels:
                cnt += 1
            if s[i-k] in vowels:
                cnt -= 1
            res_max = max(cnt, res_max)
        return res_max
        