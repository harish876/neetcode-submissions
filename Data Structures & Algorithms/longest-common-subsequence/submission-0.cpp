class Solution {
public:
    vector<vector<int>>cache;
    int lecurse(string t1, string t2,int curr1, int curr2,int n1,int n2){
        if(curr1 >= n1 || curr2 >= n2){
            return 0;
        }

        if(cache[curr1][curr2] != -1){
            return cache[curr1][curr2];
        }

        if(t1[curr1] == t2[curr2]){
            return cache[curr1][curr2] = 1 + lecurse(t1,t2,curr1+1,curr2+1,n1,n2);
        }

        else{
            return cache[curr1][curr2] = max(
                lecurse(t1,t2,curr1,curr2+1,n1,n2),
                lecurse(t1,t2,curr1+1,curr2,n1,n2)
            );
        }
    }

    int longestCommonSubsequence(string t1, string t2) {
        //classic dynammic programming problem
        //lets do the recursive first
        //then lets do the iterative one

        cache.clear();
        cache.resize(t1.size()+1,vector<int>(t2.size()+1,-1));
        return lecurse(t1,t2,0,0,t1.size(),t2.size());
    }
};
