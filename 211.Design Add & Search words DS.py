"""
Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

"""

class WordDictionary:

    def __init__(self):
        self.masternode = Node()
        self.index = 0

    def addWord(self, word: str) -> None:  # This code is similar to that of Insert from Trie
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

        insertutil(word, currnode, index)

    def search(self, word: str) -> bool:  # This code is bit different from search of Trie
        currnode = self.masternode
        index = 0
        self.res = None # Used only in case of "."

        def startsWithutil(word: str, currnode, index) -> bool:
            if index == len(word):
                if currnode.endFlag:
                    return True
                else:
                    return False
            if not currnode:
                return False
            if currnode.trielist.__contains__(word[index]):
                currnode = currnode.trielist[word[index]]
                return startsWithutil(word, currnode, index + 1)
            elif word[index] == ".":
                for eachnode in currnode.trielist.values():
                    self.res = startsWithutil(word, eachnode, index + 1)
                    if self.res: return True
                return self.res
            else:
                return False
        return startsWithutil(word, currnode, index)


class Node:
    def __init__(self, trielist=None, endFlag=False):
        if trielist is None:
            trielist = {}
        self.trielist = trielist
        self.endFlag = endFlag


word = "roshan"
word2 = "roshax"
at = "at"
andi = "and"
an = "an"
add = "add"
bat = "bat"
a = "a"
dotat = ".at"

andot = "an."
adotddot = "a.d."
bdot = "b."
adotd = "a.d"
dot = "."

node = Node()
obj = WordDictionary()

obj.addWord(word)
print("Inserted word: {}".format(word))
obj.addWord(word2)
print("Inserted word: {}".format(word2))
obj.addWord(at)
print("Inserted word: {}".format(at))
obj.addWord(andi)
print("Inserted word: {}".format(andi))
obj.addWord(an)
print("Inserted word: {}".format(an))
obj.addWord(add)
print("Inserted word: {}".format(add))

print("Whole word search! Found \"{}\"? : {}".format(a, obj.search(a)))
print("Whole word search! Found \"{}\"? : {}".format(dotat, obj.search(dotat)))
obj.addWord(bat)
print("Inserted word: {}".format(bat))
print("Whole word search! Found \"{}\"? : {}".format(dotat, obj.search(dotat)))
print("Whole word search! Found \"{}\"? : {}".format(andot, obj.search(andot)))
print("Whole word search! Found \"{}\"? : {}".format(adotddot, obj.search(adotddot)))
print("Whole word search! Found \"{}\"? : {}".format(bdot, obj.search(bdot)))
print("Whole word search! Found \"{}\"? : {}".format(adotd, obj.search(adotd)))
print("Whole word search! Found \"{}\"? : {}".format(dot, obj.search(dot)))

