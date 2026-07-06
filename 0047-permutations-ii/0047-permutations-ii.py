class Solution(object):
    def permuteUnique(self, nums):
        def reverse_(nums, a, b):
            while a < b:
                nums[a], nums[b] = nums[b], nums[a]
                a += 1
                b -= 1
        ans = []
        nums.sort()
        while True:
            ans.append(list(nums))
            i = len(nums) - 2
            while i >= 0 and nums[i] >= nums[i+1]:
                i -= 1
            if i < 0:
                return ans
            else:
                j = len(nums) - 1
                while j > i and nums[i] >= nums[j]:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
                reverse_(nums, i + 1, len(nums) - 1)

        