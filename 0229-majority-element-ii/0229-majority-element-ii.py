from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        qualified = len(nums) // 3
        cnt = Counter(nums)
        ans = []
        for key in cnt.keys():
            if cnt[key] > qualified:    ans.append(key)
        return ans