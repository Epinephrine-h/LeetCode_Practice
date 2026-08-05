class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p2s = {}
        s2p = {}
        wordList = s.split()
        if len(pattern) != len(wordList):   return False
        for ch, word in zip(pattern, wordList):
            if (ch in p2s and p2s[ch] != word) or (word in s2p and s2p[word] != ch):
                return False
            p2s[ch] = word
            s2p[word] = ch
        return True
