class Solution(object):
    def largestAltitude(self, gain):
        prefix = 0
        highest = prefix
        for i in range(len(gain)):
            prefix += gain[i]
            highest =  max(highest, prefix)
        return highest