class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        index = 0
        for num in range(nums[0], nums[-1]):
            if num != nums[index]:  ans.append(num)
            else:   index += 1
        return ans