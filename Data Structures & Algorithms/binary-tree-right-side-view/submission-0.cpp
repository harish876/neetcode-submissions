/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        if(!root){
            return {};
        }
        queue<TreeNode*>q;
        q.push(root);
        vector<int>result;
        while(!q.empty()){
            int sz = q.size();
            TreeNode *back = q.back();
            result.push_back(back->val);
            while(sz--){
                TreeNode *top = q.front();
                q.pop();
                if(top->left){
                    q.push(top->left);
                }
                if(top->right){
                    q.push(top->right);
                }
            }
        }
        return result;
    }
};