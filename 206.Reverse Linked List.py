# implemented using iteration, Also implement using recursion


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class Solution:
    def reverseList(self, head):
        if not head:
            return
        next = head.next
        curr = head
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(4)

sol = Solution()

loopnode = node
while True:
    if loopnode:
        print(loopnode.val)
        loopnode = loopnode.next
    else:
        break

revernode = sol.reverseList(node)
print("*"*40)

while True:
    if revernode:
        print(revernode.val)
        revernode = revernode.next
    else:
        break
