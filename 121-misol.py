class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        min_price = prices[0]

        for price in prices[1:]:
            min_price = min(min_price, price)
            max_price = max(max_price, price - min_price)

        return max_price