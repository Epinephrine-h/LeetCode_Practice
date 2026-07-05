class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        left = 0
        right = len(nums) - 1
        ans = 0
        while left < right:
            tmp = nums[left] + nums[right]
            if tmp < k:
                left += 1
            elif tmp > k:
                right -= 1
            else:
                ans += 1
                right -= 1
                left += 1
        return ans
