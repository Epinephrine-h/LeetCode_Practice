# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isEqual(side1, side2):
            if not side1 and not side2:     return True
            if not side1 or not side2:      return False
            return side1.val == side2.val and isEqual(side1.left, side2.right) and isEqual(side1.right, side2.left)
        return isEqual(root.left, root.right)