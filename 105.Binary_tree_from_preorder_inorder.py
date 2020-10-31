# My own version of the code.
# Optimize further by reducing the search time of finding the index, from O(n) to O(1) by using dictionary.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTreeutil(self, pre_iter, inorder):
        if len(inorder) == 0:
            return
        pre_node = TreeNode(next(pre_iter))
        in_index = inorder.index(pre_node.val)
        pre_node.left = self.buildTreeutil(pre_iter, inorder[:in_index])
        pre_node.right = self.buildTreeutil(pre_iter, inorder[in_index + 1:])

        return pre_node

    def buildTree(self, preorder, inorder) -> TreeNode:
        pre_iter = iter(preorder)
        node = self.buildTreeutil(pre_iter, inorder)

        return node


preorder = [3, 4, 1, 2, 5]
inorder = [1, 4, 2, 3, 5]

sol = Solution()
master = sol.buildTree(preorder, inorder)
print(master.val)
print(master.right.val)
print(master.left.val)
print(master.left.left.val)
print(master.left.right.val)
