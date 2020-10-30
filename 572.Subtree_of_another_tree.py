# Self written code. Not optimized code. Try to optimize the code further.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    flag = False

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def subtree_util(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False

            if s.val == t.val:
                if subtree_util(s.left, t.left):
                    return subtree_util(s.right, t.right)
            else:
                return False

        if not s or not t:
            return False

        if s.val == t.val:
            self.flag = subtree_util(s, t)

        if self.flag:
            return True

        if s.left:
            if self.isSubtree(s.left, t):
                return True

        if s.right:
            if self.isSubtree(s.right, t):
                return True

        return False

master = TreeNode(3)
master.left = TreeNode(4)
master.right = TreeNode(5)
master.left.left = TreeNode(1)
master.left.right = TreeNode(2)

subtree = TreeNode(4)
subtree.left = TreeNode(1)
subtree.right = TreeNode(2)
# subtree.right.right = TreeNode(6)
# subtree.right.right = TreeNode(7)

sol = Solution()
print(sol.isSubtree(master,subtree))
