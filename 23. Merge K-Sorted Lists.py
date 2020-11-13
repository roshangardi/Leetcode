# For K-lists, this code only uses min-heap of size "k" in a given time.
import heapq


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def mergeKLists(self, lists):
        self.index = 0  # Read https://stackoverflow.com/questions/8875706/heapq-with-custom-compare-predicate to
        # understand why index is used
        queue = []
        dummynode = Node(None)
        head = dummynode

        for node in lists:
            if not node:
                continue
            heapq.heappush(queue, (node.val, self.index, node))  # We are pushing the tuple instead of just the node in
            # the heapq because, heapq cannot compare ("<" ">") on the nodes and it needs element that accepts normal
            # Python comparisons. Hence first element in tuple is with which comparison can be made. Also, we push
            # self.index here to avoid clashes when there are duplicate node.val keys and the actual node is not
            # directly comparable - otherwise heapq could fail with TypeError. And last we also push the node itself
            self.index += 1

        while queue:
            nodeval, index, node = heapq.heappop(queue)  # Pop smallest element and Un-packing the Tuple
            if node.next:
                heapq.heappush(queue, (node.next.val, self.index, node.next))
                self.index += 1
            dummynode.next = node
            dummynode = node
        head = head.next
        return head


if __name__ == "__main__":

    node2 = Node(1)
    node3 = Node(2)
    node4 = Node(3)
    node5 = Node(1)

    node2.next = Node(4)
    node2.next.next = Node(8)
    node2.next.next.next = Node(13)

    node3.next = Node(16)
    node3.next.next = Node(18)
    node3.next.next.next = Node(99)

    node4.next = Node(12)
    node4.next.next = Node(23)
    node4.next.next.next = Node(88)

    node5.next = Node(19)
    node5.next.next = Node(53)
    node5.next.next.next = Node(80)

    mainlist = [node2, node3, node4, node5]
    # mainlist = [[]]
    # mainlist = [[],Node(1)]

    sol = Solution()
    solnode = sol.mergeKLists(mainlist)

    while solnode:
        print(solnode.val)
        solnode = solnode.next
