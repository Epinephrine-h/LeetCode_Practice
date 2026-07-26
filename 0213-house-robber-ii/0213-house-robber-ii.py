class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:  return nums[-1]
        def rob1(house):
            prev2 = prev1 = 0
            for money in house:
                curr = max(prev2 + money, prev1)
                prev2, prev1 = prev1, curr
            return prev1
        return max(rob1(nums[1:]), rob1(nums[:-1]))