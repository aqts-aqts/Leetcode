class Solution:
    def stoneGameIII(self, stoneValue):
        # To solve this problem, we will use dynamic programming
        # Let dp[i][k] be the relative score of Alice starting at row i and during player k's turn
        # If dp[i][k] < 0, Bob wins, if dp[i][k] > 0, Alice wins, otherwise the game is a tie
        # For each iteration, we will try all possible moves and take the best one (min for Bob, max for Alice)
        # To avoid recalculating the same subproblems, we will use memoization, which is the process of storing the results of subproblems so that we can use them later
        # The time complexity of this is O(n) where n is the number of stones
        # The space complexity is O(n) where n is the number of stones

        n = len(stoneValue)
        stoneValue.extend([0, 0])
        dp = [[None] * 2 for i in range(n)]
        def solve(i, k):
            if i >= n:
                return 0
            elif dp[i][k] is not None:
                return dp[i][k]
            
            if k:
                dp[i][k] = max(solve(i + 1, not k) + stoneValue[i], solve(i + 2, not k) + stoneValue[i] + stoneValue[i + 1], solve(i + 3, not k) + stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2])
            else:
                dp[i][k] = min(solve(i + 1, not k) - stoneValue[i], solve(i + 2, not k) - stoneValue[i] - stoneValue[i + 1], solve(i + 3, not k) - stoneValue[i] - stoneValue[i + 1] - stoneValue[i + 2])
            return dp[i][k]
        
        score = solve(0, 1)
        return 'Bob' if score < 0 else 'Alice' if score > 0 else 'Tie'