class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        # Let dp[i][j] be the longest chain ending on i and starting at index j of pairs

        n = len(pairs)
        pairs.sort()
        dp = {}

        def solve(i, j):
            if j == n:
                return 0
            elif (i, j) in dp:
                return dp[(i, j)]
            
            cur = pairs[j][0]
            if i < cur:
                dp[(i, j)] = max(solve(pairs[j][1], j + 1) + 1, solve(i, j + 1))
            else:
                dp[(i, j)] = solve(i, j + 1)
            
            return dp[(i, j)]
        
        return solve(-1001, 0)