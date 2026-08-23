class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest = float('inf')

        for price in prices:
            if price < lowest:
                lowest = price
            profit = price - lowest
            max_profit = max(max_profit,profit)
        return max_profit
        