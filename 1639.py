from collections import defaultdict

class word_index:
    def __init__(self):
        self.char_set = set()
        self.frequencies = defaultdict(int)
    def add_char(self, char):
        self.char_set.add(char)
        self.frequencies[char] += 1

class Solution(object):
    def numWays(self, words, target):
        # seperate each word into its characters and map them to an index
        # ["acca", "bbbb", "caca"] -> {1: set([a, b, c]), 2: set([c, b, a]), 3: set([c, b]), 4: set([a, b])}

        # solve using dp
        # let dp[k][i] be the number of ways to form target[i:] at index k
        
        n = len(words[0])
        m = len(target)

        word_map = defaultdict(word_index)

        for word in words:
            for i in range(n):
                word_map[i].add_char(word[i])
        
        dp = [[None] * m for i in range(n)]

        def solve(i, k):
            if k == m:
                return 1
            elif i == n:
                return 0
            elif dp[i][k] is not None:
                return dp[i][k]

            if target[k] in word_map[i].char_set:
                dp[i][k] = solve(i + 1, k + 1) * word_map[i].frequencies[target[k]] + solve(i + 1, k) 
            else:
                dp[i][k] = solve(i + 1, k)
            return dp[i][k]
        
        mod = 10**9 + 7
        return solve(0, 0) % mod