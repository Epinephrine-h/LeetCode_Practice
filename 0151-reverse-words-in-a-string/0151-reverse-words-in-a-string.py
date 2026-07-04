class Solution(object):
    def reverseWords(self, s):
        txt = s.split()
        txt.reverse()
        return " ".join(txt)
        