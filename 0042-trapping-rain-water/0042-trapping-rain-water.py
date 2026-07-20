class Solution:
    def trap(self, height: List[int]) -> int:
        res, left, right = 0, 0, len(height) - 1
        left_max, right_max = height[0], height[right]
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                res += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                res += right_max - height[right]
        return res