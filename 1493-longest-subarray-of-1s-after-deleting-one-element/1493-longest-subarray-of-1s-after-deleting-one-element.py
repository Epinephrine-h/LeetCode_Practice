class Solution(object):
    def longestSubarray(self, nums):
        root = 0
        ans = 0
        zero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            while zero > 1:
                if nums[root] == 0:
                    zero -= 1
                root += 1
            ans = max(ans, i - root)
        return ans
        