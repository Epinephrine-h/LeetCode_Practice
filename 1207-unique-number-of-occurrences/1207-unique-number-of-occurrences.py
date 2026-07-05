from collections import Counter
class Solution(object):
    def uniqueOccurrences(self, arr):
        select = Counter(arr)
        fre = select.values()
        return len(select) == len(set(fre))
        