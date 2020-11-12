# Merge sort:

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, node1, node2):
        if not node1 and not node2:  # If both nodes are empty, we reached end of the lists.
            return
        if not node1:  # One of the lists ran out of nodes, so now point return nodes from the second list.
            return node2  # No need to create new nodes for remaining nodes, we can just point it to existing node.
        if not node2:
            return node1

        if node1.val == node2.val:
            newnode = Node(node1.val)  # Could have also used node2, doesn't matter since node values are same
            newnode.next = self.mergeTwoLists(node1.next, node2)
            return newnode
        if node1.val < node2.val:
            newnode = Node(node1.val)  # Since node1 is small, create new node1 and increment existing one's pointer
            newnode.next = self.mergeTwoLists(node1.next, node2)  # Sending node.next / i.e. Incrementing pointer
            return newnode
        if node2.val < node1.val:
            newnode = Node(node2.val)
            newnode.next = self.mergeTwoLists(node1, node2.next)
            return newnode

    def mergesort(self, listhead):
        if not listhead:
            return listhead
        low = listhead
        high = self.findlast(listhead)
        return self.mergesortutil(low, high)

    def mergesortutil(self, low, high):
        if not low and not high:
            return
        if low == high:
            singlenode = Node(low.val)
            return singlenode
        mid, highnext = self.findmiddle(low)
        left = self.mergesortutil(low, mid)
        right = self.mergesortutil(highnext, high)
        newlist = self.mergeTwoLists(left, right)
        return newlist

    def findmiddle(self, lishead):
        slow = lishead
        fast = lishead

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        midnext = slow.next
        slow.next = None
        return (slow, midnext)

    def findlast(self, listhead):
        while listhead:
            listhead = listhead.next
        return listhead


if __name__ == "__main__":

    node2 = Node(413)
    node2.next = Node(1)
    node2.next.next = Node(13)
    node2.next.next.next = Node(8)

    sol = Solution()
    solnode = sol.mergesort(node2)

    while solnode:
        print(solnode.val)
        solnode = solnode.next
