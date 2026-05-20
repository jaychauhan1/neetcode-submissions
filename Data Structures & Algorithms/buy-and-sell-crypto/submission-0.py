class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] - lowest_price > max_profit:
                max_profit = prices[i] - lowest_price
            if lowest_price > prices[i]:
                lowest_price = prices[i]
        return max_profit
               
                

        