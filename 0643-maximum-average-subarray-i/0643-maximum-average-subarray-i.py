class Solution(object):
    def findMaxAverage(self, nums, k):
        cur_max = sum(nums[:k])
        max_sum = cur_max
        for i in range(k, len(nums)):
            cur_max -= nums[i-k]
            cur_max += nums[i]
            if cur_max > max_sum:
                max_sum = cur_max
        return float(max_sum)/k
        