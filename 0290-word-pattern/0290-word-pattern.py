class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordList = s.split()
        return len(pattern) == len(wordList) and len(set(pattern)) == len(set(wordList)) == len(set(zip(pattern, wordList)))
