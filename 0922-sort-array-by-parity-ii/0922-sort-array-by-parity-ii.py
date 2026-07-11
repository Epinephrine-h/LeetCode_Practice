class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = 0
        odd = 1
        while even < len(nums):
            if nums[even] % 2 == 1:
                while odd < len(nums) and nums[odd] % 2 == 1:
                    odd += 2
                nums[even], nums[odd] = nums[odd], nums[even]
            even += 2
        return nums