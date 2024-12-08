from collections import defaultdict, deque

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        real_wordDict = defaultdict(list)
        for word in wordDict:
            real_wordDict[word[0]].append(word)
        
        n = len(s)
        paths = []

        queue = deque([0])
        path_queue = deque([[]])
        while queue:
            idx = queue.popleft()
            path = path_queue.popleft()
            print(idx, path, n)
            
            if idx == n:
                paths.append(path)
                continue

            cur = s[idx]
            for word in real_wordDict[cur]:
                if word == s[idx:idx + len(word)]:
                    queue.append(idx + len(word))
                    path_queue.append(path + [idx + len(word)])
        
        strings = []
        for path in paths:
            string = ''
            last_idx = 0
            for i, idx in enumerate(path):
                string += s[last_idx:idx] + ('' if i == len(path) - 1 else ' ')
                last_idx = idx
            strings.append(string)
        return strings