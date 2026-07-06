class Solution(object):
    def nextPermutation(self, nums):
        def reverse_(nums, a, b):
            while a < b:
                nums[a], nums[b] = nums[b], nums[a]
                a += 1
                b -= 1
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i < 0:
            reverse_(nums, 0, len(nums) - 1)
        else:
            j = len(nums) - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            reverse_(nums, i + 1, len(nums) - 1)
        