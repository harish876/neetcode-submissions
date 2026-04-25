class TrieNode {
    public:
        unordered_map<char,TrieNode*>children;
        bool isLeaf;

        TrieNode(): isLeaf(false) {};
};

class Trie {
    private:
        TrieNode* root;
    public:
        Trie(){
            root = new TrieNode();
        }

        void insert(string word){
            TrieNode* curr = root;
            for(char c: word){
                if(curr->children.find(c) == curr->children.end()){
                    curr->children[c] = new TrieNode();
                }
                curr = curr->children[c];
            }
            curr->isLeaf = true;
        }

        bool search(string word){
            TrieNode* curr = root;
            for(char c: word){
                if(curr->children.find(c) == curr->children.end()){
                    return false;
                }
                curr = curr->children[c];
            }
            return curr->isLeaf;
        }
};

class Solution {
public:
    bool isValid(int i,int j,int m,int n){
        return (i>=0 && j>=0 && i < m && j < n);
    }
    void dfs(Trie *t,vector<vector<char>>& board,int i,int j,int m,int n,string path){
        if(!isValid(i,j,m,n) || board[i][j] == '*'){
            return;
        }  
        char c = board[i][j];
        board[i][j] = '*';
        path +=c;
        t->insert(path);
        dfs(t,board,i+1,j,m,n,path);
        dfs(t,board,i,j+1,m,n,path);
        dfs(t,board,i-1,j,m,n,path);
        dfs(t,board,i,j-1,m,n,path);
        board[i][j] = c;
        path.pop_back();
    }
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        //i want to store a list of all possible strings in a trie
        //apply search on the trie to make it efficient
        //brute force bottleneck is generating all words
        int m = board.size();
        int n = board[0].size();
        vector<string>result;
        Trie* t = new Trie();
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                dfs(t,board,i,j,m,n,"");
            }
        }
        for(auto word: words){
            if(t->search(word)){
                result.push_back(word);
            }
        }
        return result;
    }
};
