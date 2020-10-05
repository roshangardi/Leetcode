from collections import defaultdict, Counter, deque


def alienOrder(self, words: List[str]) -> str:
    # Step 1 : Build graph of words
    graph = defaultdict(set)
    indegree = Counter({c: 0 for word in words for c in word})

    # compare adjacent words
    for i in range(len(words) - 1):
        first_word = words[i]
        second_word = words[i + 1]
        for j in range(min(len(first_word), len(second_word))):
            # find the first mismatch alphabet
            if first_word[j] != second_word[j]:
                # either put the alphabet in the graph or add an edge to the graph
                if second_word[j] not in graph[first_word[j]]:
                    graph[first_word[j]].add(second_word[j])
                    # change indegree
                    indegree[second_word[j]] += 1
                break
            else:
                if len(second_word) < len(first_word): return ""
    # Step 2 : Topo Sort
    output = []
    # add elements with indegree == 0 to queue
    queue = deque([c for c in indegree if indegree[c] == 0])
    while queue:
        c = queue.popleft()
        # add to sorted order
        output.append(c)
        # change the indegrees of the end vertices and add to queue if new indegree == 0
        for d in graph[c]:
            indegree[d] -= 1
            if indegree[d] == 0:
                queue.append(d)

    # this means there was a cycle because length of our final sort is not equal to the length of items we had in the
    # indegree list
    if len(output) < len(indegree):
        return ""

    return "".join(output)
