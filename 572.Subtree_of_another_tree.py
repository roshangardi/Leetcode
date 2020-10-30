# Self written code. Not optimized code. Try to optimize the code further.
# Optimized code below
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    flag = False

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def subtree_util(s, t):
            if not (s and t):
                return True
            if not (s or t):
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


# Advanced  approach, O( | s | + | t |) (Merkle hashing): For  each node in a tree, we can create node.merkle,
# a hash representing it 's subtree. This  hash is formed by hashing the concatenation of the merkle of the left
# child, the node's value, and the merkle of the right child. Then, two trees are identical if and only if the merkle
# hash of their roots are equal (except when there is a hash collision.) From there, finding the answer is
# straightforward: we simply check if any node in s has node.merkle == t.merkle
#
# def isSubtree(self, s, t):
#     from hashlib import sha256
#     def hash_(x):
#         S = sha256()
#         S.update(x)
#         return S.hexdigest()
#
#     def merkle(node):
#         if not node:
#             return '#'
#         m_left = merkle(node.left)
#         m_right = merkle(node.right)
#         node.merkle = hash_(m_left + str(node.val) + m_right)
#         return node.merkle
#
#     merkle(s)
#     merkle(t)
#
#     def dfs(node):
#         if not node:
#             return False
#         return (node.merkle == t.merkle or
#                 dfs(node.left) or dfs(node.right))
#
#     return dfs(s)

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

