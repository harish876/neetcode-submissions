class Solution {
public:
    int characterReplacement(string s, int k) {
        /*
            k = 2
            
            X - 0
            Y - 2
            
            X Y Y Y X
                    |
                |


            0 1 2 3 4
            A A A B A B B
                |
                        |

            A - 4  
            B - 2
        */
        int n = s.size();
        int start = 0, curr = 0 ,maxFreq = 0, result = 0;
        unordered_map<int,int>mp;
        while(curr < n){
            mp[s[curr]]++;
            maxFreq = max(maxFreq,mp[s[curr]]);
            while((curr-start+1) - maxFreq > k){
                mp[s[start]]--;
                start++;
            }
            result = max(result,curr-start+1);
            curr++;
        }
        return result;
    }
};
