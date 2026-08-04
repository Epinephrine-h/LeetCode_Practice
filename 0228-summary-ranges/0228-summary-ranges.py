class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:    return []
        ans = []
        left, right = 0, 1
        while right < len(nums):
            while right < len(nums) and nums[right] == nums[right-1] + 1:      right += 1
            if left == right - 1:   ans.append(str(nums[left]))
            else: ans.append(str(nums[left]) + "->" + str(nums[right-1]))
            left = right
            right += 1
        if left == len(nums) - 1 and right == len(nums):     ans.append(str(nums[left]))
        return ans