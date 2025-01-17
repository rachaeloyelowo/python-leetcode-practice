class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        to_buy = {} # creates a dictionary of the prices to buy
        max_profit = 0 # sets the maximum profit to 0

        for i in range(len(prices)): # goes through the list of prices
            for val in to_buy.values(): # goes through each possible prices to buy
                if prices[i] - val > max_profit: # if the current price - the price to buy is greater than max profit
                    max_profit = prices[i] - val # changes it to be the new max profit
            to_buy[i] = prices[i] # adds the current price and index to be possibly bought

        return max_profit # returns the max profit