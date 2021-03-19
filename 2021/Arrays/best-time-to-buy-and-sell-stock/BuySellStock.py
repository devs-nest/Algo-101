# @Author: Kshitiz Miglani
# SDE @AMAZON | Founder @Devsnest.in
# @Link to question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class BuySellStock(object):
    def maxProfit(self, prices):
        # Keeping the pointer of minimum cost at 0th index of prices array
        # and for the time being the maximum profit is zero
        min_till_now = 100000
        best_profit = 0

        # Traversing through each element in prices array
        for price in prices:

            # if min_till_now is more than present price then update min_till_now to present price
            if min_till_now > price:
                min_till_now = price

            # If difference between the present prices and the minimum min_till_now
            # is more than previous best_profit then update it
            elif best_profit < price - min_till_now:
                best_profit = price - min_till_now

        # Answer returned here
        return best_profit
