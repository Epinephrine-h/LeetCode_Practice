class Solution(object):
    def longestOnes(self, nums, k):
        root = 0
        one = 0
        zero = 0
        ans = 0
        if k >= len(nums):
            return len(nums)
        for i in range(len(nums)):
            if nums[i] == 1:
                one += 1
            else:
                zero += 1
            while zero > k:
                if nums[root] == 1:
                    one -= 1
                else:
                    zero -= 1
                root += 1
            ans = max(ans, one + zero)
        return ans