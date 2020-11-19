# TO solve this problem we have 3 Step algorithm.
# 1) Find the middle of the linked list and divide it into 2 different linked list from the middle.
# 2) Reverse the second divided part of the linked list.
# 3) Merge both the linked list in such a manner that it takes one element from each list at a time.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or (not head.next or not head.next.next):
            return

        new_head = self.break_at_middle(head)   # Step 1
        second_head = self.reverse_list(new_head)  # Step 2
        self.merge(head, second_head)  # Step 3

    def break_at_middle(self, head):
        # using the 'slow and fast pointer' technique(used in other problems) to find the middle of the
        # linked list and then breaking the linked list at the middle.
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        new_head = slow.next    # Now slow will be pointing to middle node, and we associated new_head to slow's next
        slow.next = None    # Since we are dividing the list, we point the slow's (i.e. last node) next to None
        return new_head

    def reverse_list(self, head):
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev

    def merge(self, first_head, second_head):
        while first_head and second_head:
            f_next = first_head.next
            s_next = second_head.next

            first_head.next = second_head
            second_head.next = f_next

            first_head = f_next
            second_head = s_next


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)

sol = Solution()
sol.reorderList(node)

while node:
    print(node.val)
    node = node.next
