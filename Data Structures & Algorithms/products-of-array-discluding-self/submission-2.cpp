class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        /*
            include 1,2,4
            exclude 6


            [1, 2, 4, 6]
                   |
             1  1  2  8 
                   


            [1, 2, 4, 6]
                      
             48 24 6  1
            

            [48,24,12,8]

            -1  0   1   2   3
             1  -1  0   0   0

             3  2   1   0   -1
             0  6   6   3   1
             

        */

        //lets do the dumb approach
        int n = nums.size();
        vector<int>result(n,0);

        vector<int>pre1(n,1);
        vector<int>pre2(n,1);

        for(int i=1; i<n; i++){
            pre1[i] = nums[i-1] * pre1[i-1]; 
        }

        for(int i=n-2; i>=0; i--){
            pre2[i] = nums[i+1] * pre2[i+1];
        }

        for(int i=0; i<n; i++){
            result[i] = pre1[i] * pre2[i];
        }
        return result;

    }
};
