class Solution(object):
    def uniqueOccurrences(self, arr):
        select = set(arr)
        tmp = []
        for i in select:
            x = arr.count(i)
            if x in tmp:
                return False
            tmp.append(x)
        return True
        