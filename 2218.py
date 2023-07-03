class Solution:
    def maxValueOfCoins(self, piles, k):
        # To solve this problem, we will use dynamic programming and prefix sums to optimize the solution
        # First, we will calculate the prefix sums of each element in each pile so that we can calculate the sum of any subarray in O(1) time
        # We can't grab any coins without grabbing the ones on top, so we will just set coin i in the pile to be the sum of the first i coins in the pile
        # Then, we will use dynamic programming to find the maximum value of coins we can grab in k moves
        # For each pile, we can either grab 0 coins or grab 1 to m coins where m is the number of coins in the pile, so we will try all of these possibilities
        # To avoid recalculating the same subproblems, we will use memoization, which is the process of storing the results of subproblems so that we can use them later
        # The time complexity of this is O(nmk) where n is the number of piles, m is the maximum number of coins in a pile, and k is the number of moves
        # The space complexity is O(nk) where n is the number of piles and k is the number of moves

        n = len(piles)
        for i in range(n):
            m = len(piles[i])
            for j in range(1, m):
                piles[i][j] += piles[i][j - 1]

        dp = [[0] * (k + 1) for i in range(n + 1)]
        def solve(i, moves):
            if i == n:
                return 0
            elif moves == 0:
                return 0
            elif dp[i][moves] > 0:
                return dp[i][moves]     

            m = len(piles[i])
            dp[i][moves] = max(
                solve(i + 1, moves),
                max(
                    solve(i + 1, moves - j) + piles[i][j - 1]
                    if moves - j >= 0 else 0
                    for j in range(1, m + 1)
                )
            )
            
            return dp[i][moves]
        return solve(0, k)