class Solution:
    def canJump(self, nums: List[int]) -> bool:
        endJump = 0
        for i in range(len(nums)):
            if endJump < i:
                return False
            endJump = max(endJump, nums[i] + i)
        return True