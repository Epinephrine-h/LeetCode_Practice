# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:    return []
        queue = deque([root])
        ans= []
        l2r = False
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:   queue.append(node.left)
                if node.right:  queue.append(node.right)
            if l2r:
                tmp.reverse()
            ans.append(tmp)
            l2r = not l2r
        return ans

