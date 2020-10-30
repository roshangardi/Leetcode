# Not completely efficient, try to optimize it further.
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    ser_string = ""

    def serialize(self, root):

        if not root:
            self.ser_string += "# "
            return

        self.ser_string += str(root.val)+" "

        self.serialize(root.left)
        self.serialize(root.right)

        return self.ser_string.split(" ")

        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

    indexes = 0

    def deserialize(self, data):

        if not data:
            return None

        if self.indexes > len(data):
            return None

        if data[self.indexes] == "#" or data[self.indexes] is None:
            self.indexes += 1
            return None

        node1 = TreeNode(data[self.indexes])
        self.indexes += 1
        node1.left = self.deserialize(data)
        node1.right = self.deserialize(data)

        return node1

        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

master = TreeNode(1)
master.left = TreeNode(9)
master.right = TreeNode(2)
master.left.left = TreeNode(8)
master.left.right = TreeNode(-10)

sol = Codec()
returnvalue = sol.serialize(master)
print(returnvalue)
print(sol.deserialize(returnvalue).val)

# sol = Codec()
# returnvalue = sol.serialize(None)
# print(sol.deserialize(returnvalue))