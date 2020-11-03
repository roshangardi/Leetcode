class Trie:

    def __init__(self):
        self.trielist = {}
        self.endFlag = False
        self.next = None


    def insert(self, word: str, currnode, index) -> None:
        print("Currnode and trielist is {}".format(currnode.trielist))
        # print("Index {}".format(index))
        if index == len(word):
            currnode.endFlag = True
            return

        if not currnode:
            return

        if currnode.trielist.__contains__(word[index]):
            currnode = currnode.trielist[word[index]]
            return self.insert(word, currnode, index + 1)

        node = Node()
        currnode.trielist[word[index]] = node
        # print("Now trielist is {}".format(currnode.trielist))
        self.insert(word, node, index + 1)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """


class Node:
    def __init__(self, trielist=None, endFlag=False, next=None):
        if trielist is None:
            trielist = {}
        self.trielist = trielist
        self.endFlag = endFlag
        self.next = next


word = "roshan"
word2= "roshax"
node = Node()
obj = Trie()
obj.insert(word, node, index=0)
obj.insert(word2, node, index=0)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
