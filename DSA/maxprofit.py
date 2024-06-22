class Solution(object):
    def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        diff=0
        profit=0
        days=len(prices)
        for i in days:
            for j in range(i,days):
                diff=prices[j]-prices[i]
                if diff>=profit:
                    profit=diff
        return profit
    maxProfit([2,42,54,5,353])