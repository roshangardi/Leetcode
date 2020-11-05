# My own version/implementation of Trie. This code can't be submitted to Leetcode due to
# different definition of insert and search functions. Below this
"""
class Trie:

    def insert(self, word: str, currnode, index) -> None:
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
        self.insert(word, node, index + 1)

    def search(self, word: str, currnode, index) -> bool:
        if index == len(word):
            if currnode.endFlag == True:
                return True
            else:
                return False
        if not currnode:
            return False
        if currnode.trielist.__contains__(word[index]):
            currnode = currnode.trielist[word[index]]
            return self.search(word, currnode, index + 1)
        return False

    def startsWith(self, prefix: str, currnode, index) -> bool:
        if index == len(prefix):
            return True
        if not currnode:
            return False
        if currnode.trielist.__contains__(prefix[index]):
            currnode = currnode.trielist[prefix[index]]
            return self.startsWith(prefix, currnode, index + 1)
        return False

class Node:
    def __init__(self, trielist=None, endFlag=False, next=None):
        if trielist is None:
            trielist = {}
        self.trielist = trielist
        self.endFlag = endFlag
"""

# Modified my code for Leetcode implementation:

class Trie:

    def __init__(self):
        self.masternode = Node()
        self.index = 0

    def insert(self, word: str) -> None:
        currnode = self.masternode
        index = 0

        def insertutil(word: str, currnode, index) -> None:
            if index == len(word):
                currnode.endFlag = True
                return
            if not currnode:
                return
            if currnode.trielist.__contains__(word[index]):
                currnode = currnode.trielist[word[index]]
                return insertutil(word, currnode, index + 1)
            node = Node()
            currnode.trielist[word[index]] = node
            insertutil(word, node, index + 1)
        insertutil(word,currnode,index)
        print("Inserted word : {}".format(word))

    def search(self, word: str) -> bool:
        currnode = self.masternode
        index = 0
        def searchutil(word: str, currnode, index) -> bool:
            if index == len(word):
                if currnode.endFlag == True:
                    return True
                else:
                    return False
            if not currnode:
                return False
            if currnode.trielist.__contains__(word[index]):
                currnode = currnode.trielist[word[index]]
                return searchutil(word, currnode, index + 1)
            return False
        return searchutil(word, currnode,index)


    def startsWith(self, prefix: str) -> bool:
        currnode = self.masternode
        index = 0

        def startsWithutil(prefix: str, currnode, index) -> bool:
            if index == len(prefix):
                return True
            if not currnode:
                return False
            if currnode.trielist.__contains__(prefix[index]):
                currnode = currnode.trielist[prefix[index]]
                return startsWithutil(prefix, currnode, index + 1)
            return False

        return startsWithutil(prefix, currnode, index)


class Node:
    def __init__(self, trielist=None, endFlag=False):
        if trielist is None:
            trielist = {}
        self.trielist = trielist
        self.endFlag = endFlag

word = "roshan"
word2 = "roshax"
word3 = "ros"

node = Node()
obj = Trie()
obj.insert(word)
obj.insert(word2)

print("Whole word search! Found \"{}\"? : {}".format(word, obj.search(word)))
print("Whole word search! Found \"{}\"? : {}".format(word3, obj.search(word3)))
print("Prefix of word search! Found \"{}\"? : {}".format(word3, obj.startsWith(word3)))

"""
*************************** Succinct and Optimized code from Leetcode comments ***************************
Non-Recursive Code i.e. Iterative Code:

class TrieNode:
        # Initialize your data structure here.
        def __init__(self):
            self.word=False
            self.children={}
    
    class Trie:
    
        def __init__(self):
            self.root = TrieNode()
    
        # @param {string} word
        # @return {void}
        # Inserts a word into the trie.
        def insert(self, word):
            node=self.root
            for i in word:
                if i not in node.children:
                    node.children[i]=TrieNode()
                node=node.children[i]
            node.word=True
    
        # @param {string} word
        # @return {boolean}
        # Returns if the word is in the trie.
        def search(self, word):
            node=self.root
            for i in word:
                if i not in node.children:
                    return False
                node=node.children[i]
            return node.word
    
        # @param {string} prefix
        # @return {boolean}
        # Returns if there is any word in the trie
        # that starts with the given prefix.
        def startsWith(self, prefix):
            node=self.root
            for i in prefix:
                if i not in node.children:
                    return False
                node=node.children[i]
            return True
            
    
    # Your Trie object will be instantiated and called as such:
    # trie = Trie()
    # trie.insert("somestring")
    # trie.search("key")
"""


