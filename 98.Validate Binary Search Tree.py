"""
This problem consumed good few hours and still couldn't solve on my own.
I was trying Bottom up approach: i.e.(The current node, Left subtree and right subtree of each node should be valid bst)
Couldn't solve, Self Note: Try it again in the future and see if I can solve.
Solution from Youtube: https://www.youtube.com/watch?v=Z_-h_mpDmeg&ab_channel=KevinNaughtonJr.
Draw tree diagram for each below commented code and walk through the code for each.
Below is Top-Down Approach:
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def validate(self, root, maximum, minimum):
        if not root:
            return True
        if (maximum is not None and root.val >= maximum) or (minimum is not None and root.val <= minimum):
            return False
        else:
            return self.validate(root.left, root.val, minimum) and self.validate(root.right, maximum, root.val)

    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate(root, None, None)


# Will return False:
# master = TreeNode(5)
# master.left = TreeNode(1)
# master.right = TreeNode(4)
# master.left.left = TreeNode(8)
# master.left.right = TreeNode(9)
# master.right.left = TreeNode(3)
# master.right.right = TreeNode(6)
# master.left.left.left = TreeNode(0)

# Will return False:
# master = TreeNode(1)
# master.left = None
# master.right = TreeNode(1)

# Will return False:
# master = TreeNode(2)
# master.left = TreeNode(1)
# master.left.right = TreeNode(4)
# master.right = TreeNode(3)

# Will return True:
master = TreeNode(2)
master.left = TreeNode(1)
master.right = TreeNode(3)

sol = Solution()
print(sol.isValidBST(master))
