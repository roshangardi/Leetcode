# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        result_list = []
        if not root:
            return result_list

        from collections import deque
        queue = deque()
        queue.append(root)

        while (queue):

            level_list = []
            queue_length = len(queue)

            for i in range(queue_length):
                node = queue.popleft()
                # If you had not used deque data structure and was simple list, use                           #queue.pop(0), here 0 indicates the first element in list.
                # We are using dequeue because

                level_list.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result_list.append(level_list)

        return result_list