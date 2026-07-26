class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:  return nums[-1]
        def rob1(start, end):
            prev2 = prev1 = 0
            for money in nums[start:end]:
                curr = max(prev2 + money, prev1)
                prev2, prev1 = prev1, curr
            return prev1
        return max(rob1(1,len(nums)), rob1(0, len(nums) - 1))