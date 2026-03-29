class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # buy one day, sell in the future
        # return max profit, can be 0 if no transactions (init to 0)
        # greedy SLIDING WINDOW
        # buy price is min prices[l], prices[r] only if l < r
        # sell price is max l,r

        l = 0
        r = 1
        maxProfit = 0


        while r < len(prices):
            # is the price at r profitable? calculate and update maxp.
            if prices[l] < prices[r]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            # is the price at r lower than the current buy price? move l to r
            else:
                l = r
            r += 1
        return maxProfit
            
