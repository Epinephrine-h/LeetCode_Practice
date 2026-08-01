# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:    return 0
        q = deque([root])
        minDepth = 0
        while q:
            minDepth += 1
            for _ in range(len(q)):
                curr = q.popleft()
                if not curr.right and not curr.left:    return minDepth
                if curr.right:  q.append(curr.right)
                if curr.left:   q.append(curr.left)