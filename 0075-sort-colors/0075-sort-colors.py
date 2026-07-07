class Solution(object):
    def sortColors(self, nums):
        p0 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
        p2 = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1