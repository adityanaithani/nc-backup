class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # naive: o(n^2)
        # maxProfit = 0
        # for i in range (len(prices)):
        #     for j in range (i + 1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         print(prices[i], prices[j], profit)
        #         if profit > maxProfit:
        #             maxProfit = profit
        # return maxProfit

        # two pointers: o(n)
        # buy, sell = 0, 1
        # maxProfit = 0

        # while sell < len(prices):
        #     if prices[buy] < prices[sell]:
        #         profit = prices[sell] - prices[buy]
        #         maxProfit = max(maxProfit, profit)
        #     else: 
        #         buy = sell
        #     sell += 1
        # return maxProfit  

        # optimal: dynamic programming greedy (o(n))
        maxProfit = 0
        minBuyPrice = prices[0]

        for sell in prices:
            maxProfit = max(maxProfit, sell - minBuyPrice)
            minBuyPrice = min(minBuyPrice, sell)
        return maxProfit

            