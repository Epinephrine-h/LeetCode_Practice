class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])
        ans = -10000
        for num in nums:    ans = max(ans, num)
        return ans