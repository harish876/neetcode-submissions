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
    vector<vector<int>> levelOrder(TreeNode* root) {
        if(!root){
            return {};
        }
        vector<vector<int>>result;
        queue<TreeNode*>q;
        q.push(root);
        while(!q.empty()){
            vector<int>curr;
            int size = q.size();
            while(size--){
                TreeNode *top = q.front();
                curr.push_back(top->val);
                q.pop();
                if(top->left){
                    q.push(top->left);
                }
                if(top->right){
                    q.push(top->right);
                }
            }
            result.push_back(curr);
        }
        return result;
    }
};
