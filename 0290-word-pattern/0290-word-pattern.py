class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p2s = {}
        s2p = {}
        wordList = s.split()
        if len(pattern) != len(wordList):   return False
        for ch, word in zip(pattern, wordList):
            if ch not in p2s and word not in s2p:
                p2s[ch] = word
                s2p[word] = ch
            if ch not in p2s or word not in s2p:    return False
            if p2s[ch] == word and s2p[word] == ch: continue
            else:   return False
        return True
