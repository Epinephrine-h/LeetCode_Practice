class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        left = 1
        right = 1
        ans = [1]*n
        for i in range(n):
            ans[i] = left
            left *= nums[i]
        for i in range(n - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        return ans