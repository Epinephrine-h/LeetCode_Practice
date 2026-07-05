class Solution(object):
    def longestOnes(self, nums, k):
        root = 0
        zero = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            while zero > k:
                if nums[root] == 0:
                    zero -= 1
                root += 1
            ans = max(ans, i - root + 1)
        return ans