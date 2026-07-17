from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        ans = []
        for i in count.keys():
            if count[i] > 1:
                ans.append(i)
        return ans