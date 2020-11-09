# Came up with below solution, which I feel is not at all good, for below reason:
# 1) IMP: It changes the actual values of the linked nodes, which you don't want in most of the real word scenarios.
# 2) It's not that fast.

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
class Solution:
    def hasCycle(self, head):
        if not head:
            return False

        if head.val == "$":
            return True

        head.val = "$"
        return self.hasCycle(head.next)
"""

# Found below solution in Leetcode comments and is so awesome because it has used mathematical concept:
# It is actually Floyd's Cycle-Finding Algorithm. Also called "Tortoise and Hare Algorithm":

class Solution:
    def hasCycle(self, head):
        walker = head
        runner = head

        while runner and runner.next:   # For linked list with multiple nodes only "while runner" would have sufficed,
            walker = walker.next        # but in case of single node input "runner.next" also needs to be checked since
            runner = runner.next.next   # single node won't have next. Since runner is faster, no need to check walker.
            if walker == runner:
                return True
        return False


if __name__ == "__main__":
    node = Node(1)
    node.next = Node(9)
    node.next.next = Node(9)
    node.next.next.next = Node(9)  # Till now no cycle
    node.next.next.next.next = node.next  # Created cycle

    sol = Solution()
    print(sol.hasCycle(node))
