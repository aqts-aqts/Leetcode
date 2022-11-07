# Word Ladder
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        connections = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '-' + word[i + 1:]
                connections[pattern].append(word)

        if endWord not in wordList: return 0
        queue = deque()
        visited = defaultdict(lambda: False)
        queue.appendleft((beginWord, 1))
        visited[beginWord] = True
        while queue:
            cur, path = queue.pop()
            if cur == endWord: return path
            for i in range(len(cur)):
                pattern = cur[:i] + '-' + cur[i + 1:]
                for word in connections[pattern]:
                    if not visited[word]: queue.appendleft((word, path + 1)); visited[word] = True
        return 0