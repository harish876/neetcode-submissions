class Solution {
public:
    vector<vector<int>>result;
    void lecurse(vector<int>& nums,int curr,int n){
        if(curr >= n){
            result.push_back(nums);
            return;
        }

        for(int i=curr; i<n; i++){
            swap(nums[i],nums[curr]);
            lecurse(nums,curr+1,n);
            swap(nums[i],nums[curr]);
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        /*
              1 2 3
                  
            [2 1 3   3 2 1  1 3 2] 
            
        */
        result.clear();
        lecurse(nums,0,nums.size());
        return result;
    }
};
