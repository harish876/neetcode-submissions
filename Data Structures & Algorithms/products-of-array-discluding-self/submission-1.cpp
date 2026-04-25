class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        /*
            [1, 2, 4, 6]
            [1, 2, 8, 48]
        */

        //lets do the dumb approach
        int n = nums.size();
        vector<int>result(n,0);
        for(int i=0; i<n; i++){
            int tmp = 1;
            for(int j=0; j<n; j++){
                if(i == j ) continue;
                tmp *= nums[j];
            }
            result[i] = tmp;
        }
        return result;

    }
};
