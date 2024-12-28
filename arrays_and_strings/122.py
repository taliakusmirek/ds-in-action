# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maximum_profit = 0
        buy_day = prices[0]
        sell_day = 0 # default for comparison sake

        # The difference with this version is that if we sell, we do not finish the profit, we still have values we can traverse, account for this somehow

        # traverse the list
        for i in range(len(prices)):
            if prices[i] < buy_day: # is this the lowest element value so far?
                buy_day = prices[i] # update if so.
            else: 
                profit = prices[i] - buy_day # calculate profit based on value not being the smallest, with our smallest value
                maximum_profit += profit # add to profit total
                buy_day = prices[i] # make buy_day the next integer value
        return maximum_profit # return the maximum profit amount