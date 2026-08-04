from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:      return []
        ans = []
        word_len = len(words[0])
        word_num = len(words)
        string_len = word_len * word_num
        word_count = Counter(words)
        for i in range(word_len):
            left = i
            current_count = Counter()
            count = 0
            for right in range(i, len(s) - word_len + 1, word_len):
                sub_word = s[right:right+word_len]
                if sub_word in words:
                    current_count[sub_word] += 1
                    count += 1
                    while current_count[sub_word] > word_count[sub_word]:
                        left_word = s[left:left+word_len]
                        current_count[left_word] -= 1
                        count -= 1
                        left += word_len
                    if count == word_num:   ans.append(left)
                else:
                    current_count.clear()
                    count = 0
                    left = right + word_len
        return ans
