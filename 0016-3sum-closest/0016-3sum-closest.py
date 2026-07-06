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
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    right -= 1
                else:
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    left += 1
        return m
