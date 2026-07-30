# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node = [root]
        values = []
        i = 0
        while i < len(node):
            cur = node[i]
            values.append(cur.val)
            if cur.left:    node.append(cur.left)
            if cur.right:   node.append(cur.right)
            i += 1
        values.sort()
        return values[k - 1]