class Solution {
public:
    int maxProfit(vector<int>& prices) {
        /*
            10,1,5,6,7,1
               |     |
        */
        int n = prices.size();
        if(n == 0){
            return 0;
        }

        int minPrice = prices[0];
        int maxProfit = 0;
        for(auto it = prices.begin()+1; it != prices.end(); it++){
            int price = *it;            
            if((price - minPrice) > maxProfit){
                maxProfit = price - minPrice;
            }
            minPrice = min(minPrice,price);
        }
        return maxProfit;

    }
};
