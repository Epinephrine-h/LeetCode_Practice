class Solution(object):
    def moveZeroes(self, nums):
        left = 0
        while left < len(nums):
            while left < len(nums) and nums[left] != 0:
                left += 1
            if left == len(nums):
                return
            right = left + 1
            while right < len(nums) and nums[right] == 0:
                right += 1
            if right == len(nums):
                return
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        return
        