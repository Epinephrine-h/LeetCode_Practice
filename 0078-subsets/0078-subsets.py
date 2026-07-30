class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def subsets(start,tmp):
            ans.append(tmp)
            for i in range(start, len(nums)):
                subsets(i + 1,tmp + [nums[i]])
        subsets(0, [])
        return ans