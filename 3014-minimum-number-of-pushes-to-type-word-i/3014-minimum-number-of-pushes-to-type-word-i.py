class Solution:
    def minimumPushes(self, word: str) -> int:
        if len(word) < 9:   return len(word)
        if len(word) < 17:  return 8 + 2 * (len(word) - 8)
        if len(word) < 25:  return 24 + 3 * (len(word) - 16)
        return 48 + (len(word) - 24) * 4