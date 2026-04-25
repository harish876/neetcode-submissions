class Solution {
public:
    vector<vector<int>>cache;
    int dfs(string word1,string word2,int i,int j){
        if(i >= word1.size()){
            return word2.size() - j;
        }

        if(j >= word2.size()){
            return word1.size() - i;
        }

        if(cache[i][j] != -1){
            return cache[i][j];
        }

        if(word1[i] == word2[j]){
            return cache[i][j] = dfs(word1,word2,i+1,j+1);
        }
        else{
            return cache[i][j] = min(
                min(
                    1 + dfs(word1,word2,i,j+1),
                    1 + dfs(word1,word2,i+1,j)
                ),
                1 + dfs(word1,word2,i+1,j+1)
            );
        }
    }
    int minDistance(string word1, string word2) {
        /*
            monkeys
                  |
            money
                 |
        */
        cache.clear();
        cache.resize(word1.size()+1,vector<int>(word2.size(),-1));
        return dfs(word1,word2,0,0);
    }
};
