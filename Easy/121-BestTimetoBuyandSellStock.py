from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        lowest_price = float("inf")

        for idx, price in enumerate(prices):
            lowest_price = min(lowest_price, price)
            max_profit = max(max_profit, price - lowest_price)

        return max_profit
