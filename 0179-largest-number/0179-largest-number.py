from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            return 0
        str_nums = [str(num) for num in nums]
        str_nums.sort(key = cmp_to_key(compare))
        res = "".join(str_nums)
        return "0" if res[0] == "0" else res