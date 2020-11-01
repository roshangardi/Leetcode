"""Most initial Solution by me:

class Solution:
    result = []

    def kthSmallestutil(self, root: TreeNode, k) -> int:
        if len(self.result) >= k:  # If k is small, no need to store all numbers in list, helps reduce space complexity
            return
        if not root:
            return
        else:
            self.kthSmallestutil(root.left, k)
            self.result.append(root.val)
            self.kthSmallestutil(root.right, k)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.kthSmallestutil(root, k)
        return self.result[k - 1]

This code has 2 problems:
1) It is working locally but on leetcode it is giving wrong output. (Try to figure out why)
2) It is storing nodes in result LIST unnecessarily, which increases space complexity. Below approach just
decrements the k value till it reaches zero and then returns that result. So zero space utilization.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def kthSmallestutil(self, root: TreeNode) -> int:
        if self.found:  # To exit as soon as possible
            return
        if not root:
            return
        self.kthSmallestutil(root.left)
        self.k -= 1
        if self.k == 0:
            self.result = root.val
            self.found = True
            return
        self.kthSmallestutil(root.right)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.result = None
        self.found = False  # To exit as soon as possible
        self.k = k
        self.kthSmallestutil(root)
        return self.result


master = TreeNode(4)
master.left = TreeNode(2)
master.right = TreeNode(6)
master.right.right = TreeNode(7)
master.right.left = TreeNode(5)
master.left.left = TreeNode(1)
master.left.right = TreeNode(3)

sol = Solution()
print(sol.kthSmallest(master, 2))
