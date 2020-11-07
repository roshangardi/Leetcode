# In this code search_dfs is the most important function where the actual logic resides
# First thing to notice is the arguments that are send to that search_dfs function and
# think about why those arguments were chosen/needed by that function.

# We have multiple such 2D matrix problems like "Number of Islands" etc. But in this problem, we already know the
# words that needs to be searched and hence we can use Trie data structure which is efficient. But in case of
# "Number of Island" problem a simple DFS(for Graph theory) was able to solve it. And also Trie cannot be used there
# since you don't have already known value(like words) to insert and then search.

class Solution:
    def __init__(self):
        self.masternode = Node()
        self.index = 0
        self.answer = []

    def insert(self, word: str) -> None:
        currnode = self.masternode
        index = 0

        def insertutil(word: str, currnode, index, nodeword) -> None:
            if index == len(word):
                currnode.endFlag = True
                return
            if not currnode:
                return
            if currnode.trielist.__contains__(word[index]):
                currnode = currnode.trielist[word[index]]
                return insertutil(word, currnode, index + 1, currnode.word)
            node = Node()
            node.word += nodeword + word[index]
            print(node.word)
            currnode.trielist[word[index]] = node
            insertutil(word, node, index + 1, node.word)

        insertutil(word, currnode, index, currnode.word)
        print("Inserted word : {}".format(word))

    def findWords(self, board, words):
        for word in words:
            self.insert(word)
        for row in range(len(board)):
            for col in range(len(board[row])):
                self.search_dfs(board, row, col, len(board), len(board[row]), self.answer, self.masternode)
        return self.answer

    def search_dfs(self, board, row, col, rowlength, collength, temp_ans, currnode):
        if board[row][col] == "$" or not currnode.trielist.__contains__(board[row][col]):
            return

        currnode = currnode.trielist[board[row][col]]

        if currnode.endFlag:
            temp_ans.append(currnode.word)
            currnode.endFlag = False

        char = board[row][col]  # Temporarily store current character, since we have change back "$" to character
        board[row][col] = "$"   # Mark current node visited

        if row > 0:
            self.search_dfs(board, row - 1, col, rowlength, collength, temp_ans, currnode)
        if row < rowlength-1:
            self.search_dfs(board, row + 1, col, rowlength, collength, temp_ans, currnode)
        if col > 0:
            self.search_dfs(board, row, col - 1, rowlength, collength, temp_ans, currnode)
        if col < collength-1:
            self.search_dfs(board, row, col + 1, rowlength, collength, temp_ans, currnode)

        board[row][col] = char  # Mark current node unvisited by restoring value.

class Node:
    def __init__(self, trielist=None, endFlag=False):
        if trielist is None:
            trielist = {}
        self.trielist = trielist
        self.endFlag = endFlag
        self.word = ""


board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]  # Words to be searched in the above board

node = Node()
sol = Solution()
print("From the given words, found following words in the board: {}".format(sol.findWords(board, words)))