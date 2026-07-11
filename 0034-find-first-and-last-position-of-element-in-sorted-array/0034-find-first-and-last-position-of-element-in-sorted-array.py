class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 1:
            return [-1,-1]
        def binarySearch(task):
            left = 0
            right = len(nums) - 1
            ans = -1
            while left <= right:
                mid = int((left + right) / 2)
                if nums[mid] == target:
                    ans = mid
                    if task == "first":     right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return ans
        return [binarySearch("first"), binarySearch("last")]
        