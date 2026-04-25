class Solution {
public:

    int numOfDigits(int k)
    {
        int result = 0;
        if (k == 0)
        {
            return 1;
        }
        while (k != 0)
        {
            result += 1;
            k /= 10;
        }
        return result;
    }

    string encode(vector<string>& strs) {
        string res = "";
        for(string s:strs){
            int n = s.size();
            res+= to_string(numOfDigits(n)) + to_string(n) + s;
        }
        cout<<res<<endl;
        return res;
    }

    vector<string> decode(string s)
    {
        vector<string> result;
        int n = s.size();
        int i = 0;
        while (i < n)
        {
            int lenSize = s[i] - '0';
            i += 1;

            string lenStr = "";
            for (int k = 0; k < lenSize; k++)
            {
                lenStr += s[i + k];
            }

            int len = stoi(lenStr);
            i += lenSize;
            string tmp = "";
            for (int j = 0; j < len; j++)
            {
                tmp += s[i + j];
            }
            result.push_back(tmp);
            i += len;
        }
        return result;
    }
};
