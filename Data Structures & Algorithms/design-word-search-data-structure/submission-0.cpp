class TrieNode {
    public:
        unordered_map<char,TrieNode*>children;
        bool isLeaf;

        TrieNode(): isLeaf(false) {};
};

class WordDictionary {
private:
    TrieNode* root;
public:
    WordDictionary() {
        root = new TrieNode();
    }
    
    void addWord(string word) {
        TrieNode* curr = root;
        for(char c: word){
            if(curr->children.find(c) == curr->children.end()){
                curr->children[c] = new TrieNode();
            }
            curr = curr->children[c];
        }
        curr->isLeaf = true;
    }
    
    bool helper(string word,int i,TrieNode* curr){
        if(i >= word.size()){
            return curr->isLeaf;
        }

        bool ans = false;

        if(word[i] == '.'){
            for(auto child: curr->children){
                ans |= helper(word,i+1,child.second);
            }
        }
        else{
            if(curr->children.find(word[i]) == curr->children.end()){
                return false;
            }
            ans |= helper(word,i+1,curr->children[word[i]]);
        }
        return ans;
    }

    bool search(string word) {
        TrieNode* curr = root;
        return helper(word,0,curr);
    }
};
