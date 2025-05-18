class Solution {
    public int maximumProfit(int prices[]) {
        // code here
        int ans = 0;
        int n = prices.length;
        
        for(int i=1; i<n; i++)
        {
            if(prices[i]>prices[i-1])
            {
                int a = prices[i] - prices[i-1];
                ans = ans + a;
            }
        }
        return ans;
    }
}