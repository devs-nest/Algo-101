class Solution //By CyFun
{
public:
    int maxProfit(vector<int> &prices)
    {
        int max_profit = 0, min_price = INT_MAX;

        for (int &price : prices)
        {
            // Min priced stock so far
            min_price = min(min_price, price);
            // profit if stock is sold at current price
            max_profit = max(max_profit, price - min_price);
        }
        return max_profit;
    }
};