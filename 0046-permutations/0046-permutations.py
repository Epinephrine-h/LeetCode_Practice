class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def reverse_(a, b):
            while a < b:
                nums[a], nums[b] = nums[b], nums[a]
                a += 1
                b -= 1
        ans = []
        if len(nums) == 1:
            return [nums]
        nums.sort()
        while True:
            ans.append(list(nums))
            i = len(nums) - 2
            while i >= 0 and nums[i] > nums[i+1]:
                i -= 1
            if i < 0:
                break
            else:
                j = len(nums) - 1
                while j > i and nums[j] <= nums[i]:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
                reverse_(i + 1, len(nums) - 1)
        return ans