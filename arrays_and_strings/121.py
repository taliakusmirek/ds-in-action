# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maximum_profit = 0
        buy_day = prices[0]
        sell_day = 0 # default for comparison sake
        # traverse the list
        for i in range(len(prices)):
            if prices[i] < buy_day: # is this the lowest element value so far?
                buy_day = prices[i] # update if so.
            else: 
                profit = prices[i] - buy_day # calculate profit based on value not being the smallest, with our smallest value
                if maximum_profit < profit: # if its the maximum value we can get, update maximum profit
                    maximum_profit = profit
        return maximum_profit # return the maximum profit amount

