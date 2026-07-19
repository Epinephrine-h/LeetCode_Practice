class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse = True)
        total, left = sum(nums), 0
        for i in range(len(nums)):
            left += nums[i]
            if left > total - left:
                return nums[:i+1]