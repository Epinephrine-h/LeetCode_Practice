class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        res = float('-inf')
        while left < right:
            res = max(res, min(height[left], height[right]) * (right - left))
            if height[left] == height[right]:
                left += 1
                right -= 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return res

        