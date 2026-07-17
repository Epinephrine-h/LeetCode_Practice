class Solution:
    def sortSentence(self, s: str) -> str:
        texts = sorted(s.split(), key = lambda x : x[-1])
        word = [t.replace(t[-1], "") for t in texts]
        return " ".join(word)