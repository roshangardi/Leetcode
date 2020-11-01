# Solution is easy in case of BST, but difficult for Binary Tree. Think how you would solve if it was a Binary Tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

master = TreeNode(4)
master.left = TreeNode(2)
master.right = TreeNode(6)
master.right.right = TreeNode(7)
master.right.left = TreeNode(5)
master.left.left = TreeNode(1)
master.left.right = TreeNode(3)

p = master.right
q = master.right.right

sol = Solution()
result_node = sol.lowestCommonAncestor(master, p, q)
print(result_node.val)
