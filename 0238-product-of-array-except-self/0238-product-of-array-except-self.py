class Solution(object):
    def productExceptSelf(self, nums):
        left = []
        right = []
        left.append(1)
        ans = []
        right.append(1)
        for i in range(len(nums)):
            left.append(left[i] * nums[i])
        nums.reverse()
        for i in range(len(nums)):
            right.append(right[i] * nums[i])
        right.reverse()
        for i in range(len(nums)):
            ans.append(left[i] * right[i + 1])
        return ans