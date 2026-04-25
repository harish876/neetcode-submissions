class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        /*
            1 2 3 2 2
            0 1 2 3 4
        */
        int curr = 0;
        int n = nums.size();
        unordered_set<int>seen;
        while(curr < n){
            if(seen.find(nums[curr]) != seen.end()){
                return nums[curr];
            }
            seen.insert(nums[curr]);
            curr = nums[curr];
        }
    }
};
