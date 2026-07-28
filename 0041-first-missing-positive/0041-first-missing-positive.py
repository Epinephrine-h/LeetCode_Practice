class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        inf = len(nums) + 1
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):      nums[i] = inf
        for num in nums:
            if abs(num) <= len(nums):
                index = abs(num) - 1
                nums[index] = -abs(nums[index])
        for i in range(len(nums)):
            if nums[i] > 0:    return i + 1
        return inf