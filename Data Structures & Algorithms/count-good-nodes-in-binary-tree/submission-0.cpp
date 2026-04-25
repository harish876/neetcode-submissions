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
    int helper(TreeNode* root, int maxLeastElement){
        if(!root){
            return 0;
        }
        if(root->val >= maxLeastElement){
            maxLeastElement = root->val;
            return 1 + helper(root->left,maxLeastElement) + helper(root->right,maxLeastElement);
        }
        return helper(root->left,maxLeastElement) + helper(root->right,maxLeastElement);

    }

    int goodNodes(TreeNode* root) {
        //maintain the max least element in the path
        return helper(root,root->val);
    }
};