class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        completetion = set(x for x in range(nums[0], nums[-1]))
        return sorted(completetion - set(nums))