class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit is basically prices[i] = prices[i-x]
        # naive: buy first day then try selling every day, store max value, loop
        maxProfit = 0
        for i in range (len(prices)):
            for j in range (i + 1, len(prices)):
                profit = prices[j] - prices[i]
                # print(prices[i], prices[j], profit)
                if profit > maxProfit:
                    maxProfit = profit
        return maxProfit
            