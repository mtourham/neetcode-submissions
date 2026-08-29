class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        profit = 0
        while j < len(prices):
            if (prices[i] > prices[j]):
                i = j
            elif (profit < (prices[j] - prices[i])):
                profit = prices[j] - prices[i]
            j += 1
        return profit
            