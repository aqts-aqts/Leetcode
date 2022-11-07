# Candy
class Solution:
    def candy(self, ratings):
        n = len(ratings)
        candies = [1] * n
        for i in range(n):
            if i - 1 >= 0 and i + 1 < n and ratings[i] > ratings[i - 1] and ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i - 1], candies[i + 1]) + 1
            elif i - 1 >= 0 and ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
            elif i + 1 < n and ratings[i] > ratings[i + 1]:
                candies[i] = candies[i + 1] + 1
        for i in range(n - 1, -1, -1):
            if i - 1 >= 0 and i + 1 < n and ratings[i] > ratings[i - 1] and ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i - 1], candies[i + 1]) + 1
            elif i - 1 >= 0 and ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
            elif i + 1 < n and ratings[i] > ratings[i + 1]:
                candies[i] = candies[i + 1] + 1
        return sum(candies)