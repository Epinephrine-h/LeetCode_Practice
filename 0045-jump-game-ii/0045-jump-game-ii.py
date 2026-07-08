class Solution:
    def jump(self, nums: List[int]) -> int:
        jmp = 0
        f = 0
        endJump = 0
        for i in range(len(nums)-1):
            f = max(f, nums[i] + i)
            if i == endJump:
                endJump = f
                jmp += 1
        return jmp