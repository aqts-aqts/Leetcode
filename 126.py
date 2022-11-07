# Word Ladder II
import sys
from collections import deque, defaultdict

paths = set()
def dfs(connections, distance, beginWord, cur, path=None, visited=None):
    if path is None: path = []
    if visited is None: visited = set()
    path.append(cur)
    visited.add(cur)
    if cur == beginWord: paths.add(tuple(reversed(path)))
    for i in range(len(cur)):
        pattern = cur[:i] + '-' + cur[i + 1:]
        for word in connections[pattern]:
            if word not in visited:
                if distance[word] == distance[cur] - 1: dfs(connections, distance, beginWord, word, path.copy(), visited.copy())

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordList.append(beginWord)
        connections = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '-' + word[i + 1:]
                connections[pattern].append(word)
        distance = defaultdict(lambda: sys.maxsize)
        visited = defaultdict(lambda: False)
        queue = deque()
        queue.appendleft(beginWord)
        distance[beginWord] = 0
        visited[beginWord] = True
        while queue:
            cur = queue.pop()
            for i in range(len(cur)):
                pattern = cur[:i] + '-' + cur[i + 1:]
                for word in connections[pattern]:
                    if not visited[word]:
                        queue.appendleft(word)
                        visited[word] = True
                        distance[word] = distance[cur] + 1
        global paths
        paths = set()
        dfs(connections, distance, beginWord, endWord)
        return list(paths)