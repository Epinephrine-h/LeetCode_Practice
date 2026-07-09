class Solution:
    def canJump(self, nums: List[int]) -> bool:
        endJump = 0
        for i in range(len(nums) - 1):
            endJump = max(nums[i] + i, endJump)
            if endJump == i:
                return False
        return True