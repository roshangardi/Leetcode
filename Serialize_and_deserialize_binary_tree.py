# Optimized Code || Check Git history for previous version of slower code.
# Here we learned about defining function inside another function.
# Also most important is how we avoid use "for loop" by using iter built in function to iterate through the list.
# Because "for loop" wouldn't work in this scenario due to use of recursion.
# We can get through this also using global index and increment it with every recursion, but iter is better&cleaner.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        def serialize_util(node):
            if not node:
                temp_list.append("#")
            else:
                temp_list.append(str(node.val))
                serialize_util(node.left)
                serialize_util(node.right)
        temp_list = []
        serialize_util(root)
        return ' '.join(temp_list)

    def deserialize(self, data):
        def deserialize_util():
            val = next(list_iterator)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = deserialize_util()
            node.right = deserialize_util()
            return node
        temp_list = data.split(" ")
        list_iterator = iter(temp_list)
        return deserialize_util()

master = TreeNode(1)
master.left = TreeNode(9)
master.right = TreeNode(2)
master.left.left = TreeNode(8)
master.left.right = TreeNode(-10)

sol = Codec()
returnvalue = sol.serialize(master)
print(returnvalue)
print(sol.deserialize(returnvalue).val)
