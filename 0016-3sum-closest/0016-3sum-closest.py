class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        m = float('inf')
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if abs(sum - target) < abs(m - target):
                    m = sum
                if sum == target:
                    return target
                elif sum > target:
                    right -= 1
                else:
                    left += 1
        return m
