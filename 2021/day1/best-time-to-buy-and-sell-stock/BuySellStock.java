/**
 * @Author: Araika Singh <NonZeroExitCode>
 * @Date:   2021-03-19T20:58:27+05:30
 * @Email:  roseymods@gmail.com
 * @Last modified by:   NonZeroExitCode
 * @Last modified time: 2021-03-20T01:27:49+05:30
 * @Link to question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
 */

class BuySellStock{

  public int maxProfit(int[] prices) {
    // Keeping the pointer of minimum cost at 0th index of prices array
    // and for the time being the maximum profit is zero
    int minCost = prices[0], maxProfit = 0;

    // Traversing through each element in prices array
    for(int i = 1; i < prices.length; i++){

      // if minCost is more than present price then update minCost to prices[i]
      minCost = Math.min(minCost, prices[i]);

      // If difference between the present prices and the minimum minCost
      // is more than previous maxProfit then update it
      maxProfit = Math.max(maxProfit, prices[i]-minCost);
    }

    // Answer returned here
    return maxProfit;
    }
}
