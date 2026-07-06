class Solution(object):
    def longestCommonPrefix(self, strs):
        ans = strs[0]
        for i in range(len(ans)):
            char = ans[i]
            for word in strs[1:]:
                if i >= len(word) or word[i] != char:
                    return ans[:i]
        return ans