class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        ans = 0
        min_price = 10**4

        for p in prices:
            if p < min_price:
                min_price = p

            if p - min_price > ans:
                ans = p - min_price

        return ans
