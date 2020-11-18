# Created my own code to delete Nth node from the last of the LinkedList.
# Note: Try to make use of dummy nodes to get rid of corner cases like empty list or single node list etc.
# This is not a good solution considering first reversing and then traversing of the list and then again reversing.
# So a better solution is a simple math trick to find correct node to delete, with slow and fast pointers. Check last code.
""" My own Code:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next:   # If it has more than one element in the list, else just return empty list in case of only one node.
            lastnode = self.reverselist(head, None) # Reverse the linkedlist.
            if n > 1:   # If the node to be removed is the last node, just delete the last node, else go to deleteme function.
                self.deleteme(lastnode, None, 1, n)
            else:
                lastnode = lastnode.next    # Again reverse the Linkedlist.
            firstnode = self.reverselist(lastnode, None)
            return firstnode
        else:
            return

    def reverselist(self, currnode, prev):
        self.lastnode = None
        self.flag = None
        if not currnode:
            self.flag = True
            return
        nextnode = currnode.next
        currnode.next = prev
        prev = currnode

        self.reverselist(nextnode, prev)
        if self.flag:
            self.lastnode = currnode
            self.flag = False
        return self.lastnode

    def deleteme(self, curr_node, prev, count, n):
        if count == n:
            prev.next = curr_node.next
            return
        prev = curr_node
        count += 1
        self.deleteme(curr_node.next, prev, count, n)


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)

sol = Solution()
head = sol.removeNthFromEnd(node, 2)  # Here 2 is the nth node from last. (2nd node from last)

while head:
    print(head.val)
    head = head.next
"""


# Optimized code:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """In this code we are keeping 'n' distance between both pointers and incrementing both at constant speed,
    and when fast pointer reaches beyond last node/None value, it is similar to having
    'n' distance from the end till the slow pointer and then we can delete node at slow pointer"""

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_node = ListNode(-1)
        dummy_node.next = head

        slow = dummy_node  # Point this to dummy_node and not Head, else in case of only two nodes, it will give error.
        fast = dummy_node

        for i in range(n + 1):  # Using dummy node, hence extra 1 (i.e. n+1)
            fast = fast.next  # keep distance 'n' between fast and slow pointer

        while fast:  # Then increment both with equal speed
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next  # Remove the node by pointing to it's next.
        return dummy_node.next  # Returning the actual head.


node = ListNode(1)
node.next = ListNode(2)
# node.next.next = ListNode(3)

sol = Solution()
head = sol.removeNthFromEnd(node, 2)  # Here 2 is the nth node from last. (2nd node from last)

while head:
    print(head.val)
    head = head.next
