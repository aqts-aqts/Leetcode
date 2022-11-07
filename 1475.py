# Final Prices With a Special Discount in a Shop
class Solution:
    def finalPrices(self, prices):
        def findNext(i):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]: return prices[j]
            return 0
        totals = []
        for index, price in enumerate(prices):
            discount = findNext(index)
            totals.append(price - discount)
        return totals