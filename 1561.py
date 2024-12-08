from collections import deque

class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        # Greedy method: Pick the max 2 numbers for the first and second coins, and the min number for the last number.
        coins = 0
        piles = deque(sorted(piles))

        while piles:
            bob = piles.popleft()
            alice = piles.pop()
            you = piles.pop()

            coins += you
        return coins