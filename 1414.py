class Solution:
    def __init__(self):
        self.dp = {}

    def findFibonacciNumber(self, i: int) -> int:
        if i == 0:
            return 0
        if i == 1:
            return 1
        if i in self.dp:
            return self.dp[i]

        self.dp[i] = self.findFibonacciNumber(i - 1) + self.findFibonacciNumber(i - 2)
        return self.dp[i]

    def findLargestFibonacciNumberLessThanK(self, k: int) -> int:
        i = 0
        while self.findFibonacciNumber(i) <= k:
            i += 1
        return self.findFibonacciNumber(i - 1)

    def findMinFibonacciNumbers(self, k: int) -> int:
        # Greedy method
        # Find the largest fibonacci number that is smaller than k and subtract it from k
        # Repeat until k is 0
 
        numbers = 0
        while k > 0:
            k -= self.findLargestFibonacciNumberLessThanK(k)
            numbers += 1
        return numbers