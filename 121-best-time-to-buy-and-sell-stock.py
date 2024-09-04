class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n^2)
        # max_profit = float('-inf')

        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         if profit > 0:
        #              max_profit = max(max_profit, profit)
        
        # return max_profit if max_profit > float('-inf') else 0

        min_price = float("inf")
        max_profit = 0

        for i in prices:
            if i < min_price:
                min_price = i
            
            profit = i - min_price
            if profit > max_profit:
                max_profit = profit
                
        return max_profit