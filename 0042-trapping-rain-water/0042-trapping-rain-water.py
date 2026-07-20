class Solution:
    def trap(self, height: List[int]) -> int:
        res, left, right = 0, 0, [0]*len(height)
        right[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            if height[i] < right[i+1]:
                right[i] = right[i+1]
            else:
                right[i] = height[i]
        for i in range(len(height)):
            left = max(left, height[i])
            res += min(right[i], left) - height[i]
        return res