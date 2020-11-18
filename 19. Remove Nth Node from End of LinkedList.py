# Created my own code to delete Nth node from the last of the LinkedList.


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
