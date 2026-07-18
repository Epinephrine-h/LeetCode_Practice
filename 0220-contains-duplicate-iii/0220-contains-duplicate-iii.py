class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        bucket = {}
        w = valueDiff + 1
        for i,num in enumerate(nums):
            x = num // w
            if x in bucket:
                return True
            if (x - 1) in bucket and abs(num - bucket[x - 1]) <= valueDiff:
                return True
            if (x + 1) in bucket and abs(num - bucket[x + 1]) <= valueDiff:
                return True
            bucket[x] = num
            if i >= indexDiff:
                old_num = nums[i - indexDiff]
                old_x = old_num // w
                del bucket[old_x]
        return False
        