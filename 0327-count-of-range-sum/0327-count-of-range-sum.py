class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix_sum = [0]
        for i in range(len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        def mergeSort(left, right):
            if right - left <= 1:
                return 0
            mid = (left + right) // 2
            count = mergeSort(left, mid) + mergeSort(mid,right)
            i = j = mid
            for left_val in prefix_sum[left:mid]:
                while i < right and prefix_sum[i] - left_val < lower:
                    i += 1
                while j < right and prefix_sum[j] - left_val <= upper:
                    j += 1
                count += (j - i)
            prefix_sum[left:right] = sorted(prefix_sum[left:right])
            return count
        return mergeSort(0, len(prefix_sum))
            