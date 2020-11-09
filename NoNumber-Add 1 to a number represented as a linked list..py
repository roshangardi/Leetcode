# I implemented using DFS, check below comments for iterative approach.


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class Solution:
    def __init__(self):
        self.carry = 1

    def addition(self, head):
        reverse_head = self.reverseList(head)  # Step 1

        self.additionutil(reverse_head, temp=None)  # Step 2

        original_head = self.reverseList(reverse_head)  # Step 3
        return original_head

    def additionutil(self, head, temp):
        if not head and self.carry == 1:
            newnode = Node(self.carry)
            temp.next = newnode
            return
        if not head:
            return

        sum = self.carry + head.val
        if sum >= 10:
            self.carry = 1
        else:
            self.carry = 0
        sum = sum % 10
        head.val = sum
        temp = head

        if self.carry == 1:
            self.additionutil(head.next, temp)
        else:
            return

    def reverseList(self, head):
        if not head:
            return
        curr = head
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


node = Node(1)
node.next = Node(9)
node.next.next = Node(9)
node.next.next.next = Node(9)

sol = Solution()

loopnode = node
print("Original Number:")
while True:
    if loopnode:
        print(loopnode.val)
        loopnode = loopnode.next
    else:
        break

revernode = sol.addition(node)

print("Original Number plus one:")
while True:
    if revernode:
        print(revernode.val)
        revernode = revernode.next
    else:
        break

"""
Iterative Approach of same code in C++:

Node *addOneUtil(Node *head) {
   Node* result = head;
   Node *temp, *p = NULL;
   int carry = 1, sum;

   while (head != NULL) {
      sum = carry + head->data;
      carry = (sum >= 10)? 1 : 0;
      sum = sum % 10;
      head->data = sum;
      temp = head;
      head = head->n;
   }
   if (carry > 0)
      temp->next = newNode(carry);
   return result;

Node* addOne(Node *head) {
   head = reverse(head); # Reverse is same as DFS implementation so not included in iterative approach.
   head = addOneUtil(head);
   return reverse(head);
}

}
"""