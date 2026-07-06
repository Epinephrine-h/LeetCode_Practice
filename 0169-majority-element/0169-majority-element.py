class Solution(object):
    def majorityElement(self, nums):
        candidate = None
        cnt = 0
        for i in nums:
            if cnt == 0:
                candidate = i
            cnt += 1 if candidate == i else -1
        return candidate
        