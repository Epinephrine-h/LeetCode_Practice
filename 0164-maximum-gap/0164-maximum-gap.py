class Solution(object):
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        nums.sort()
        ans = float('-inf')
        for i in range(1,len(nums)):
            ans = max(ans, nums[i] - nums[i-1])
        return ans
        