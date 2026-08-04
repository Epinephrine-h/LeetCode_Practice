from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        qualified = len(nums) // 3
        cnt = Counter(nums)
        ans = []
        for num, fre in cnt.items():
            if fre > qualified:    ans.append(num)
        return ans