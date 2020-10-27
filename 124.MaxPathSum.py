# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.result = float('-inf')  # a number smaller than all others, inf-> minus infinity
        self.pathSumUtil(root, self.result)
        return self.result

    def pathSumUtil(self, root, result):
        if not root:
            return 0

        left = self.pathSumUtil(root.left, result)
        right = self.pathSumUtil(root.right, result)

        max_straight = max(max(left, right) + root.val, root.val)
        max_triangle = max(max_straight, left + right + root.val)
        self.result = max(self.result, max_triangle)

        return max_straight