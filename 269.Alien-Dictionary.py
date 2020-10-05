# Python3

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def __init__(self):
        self.node_map = {}

    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):

        # approach: DFS with recursion

        if not node:
            return None

        if node.label in self.node_map:
            return self.node_map[node.label]

        copy_node = UndirectedGraphNode(node.label)
        self.node_map[node.label] = copy_node

        for neighbor in node.neighbors:
            copy_node.neighbors.append(self.cloneGraph(neighbor))

        return copy_node