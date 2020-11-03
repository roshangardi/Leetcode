# This algorithm not only works for 2 node (i.e p and q) but can work for any number of nodes to
# find the ancestor of all those nodes. Just add the nodes in function definition.

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        if not left and not right:
            return None

        if left:
            return left
        else:
            return right


master = TreeNode(4)
master.left = TreeNode(2)
master.right = TreeNode(6)
master.right.right = TreeNode(7)
master.right.left = TreeNode(5)
master.left.left = TreeNode(1)
master.left.right = TreeNode(3)

p = master.left
q = master.left.right

sol = Solution()
result_node = sol.lowestCommonAncestor(master, p, q)
print("Result : {}".format(result_node.val))

"""
Something a genius would do: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65225/4-lines-C%2B%2BJavaPythonRuby

def lowestCommonAncestor(self, root, p, q):
    if root in (None, p, q): return root
    left, right = (self.lowestCommonAncestor(kid, p, q)
                   for kid in (root.left, root.right))
    return root if left and right else left or right
    
Or using that None is considered smaller than any node:

def lowestCommonAncestor(self, root, p, q):
    if root in (None, p, q): return root
    subs = [self.lowestCommonAncestor(kid, p, q)
            for kid in (root.left, root.right)]
    return root if all(subs) else max(subs)
"""