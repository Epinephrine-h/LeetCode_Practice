class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left + 1 < len(nums) and nums[left] == nums[left+1]:
                        left += 1
                    while right > 0 and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum > 0:
                    right -= 1
                else:
                    left += 1
        return ans
        