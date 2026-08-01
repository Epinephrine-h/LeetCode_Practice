# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:    return []
        ans = []
        queue = [root]
        while queue:
            ansTmp = []
            tmp = []
            for nodes in queue:
                ansTmp.append(nodes.val)
                if nodes.left:      tmp.append(nodes.left)
                if nodes.right:     tmp.append(nodes.right)
            ans.append(ansTmp)
            queue = tmp
        return ans[::-1]
