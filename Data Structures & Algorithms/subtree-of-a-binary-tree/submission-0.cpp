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
    bool helper(TreeNode *p, TreeNode *q){
        if(!p && !q){
            return true;
        }
        else if((p && !q) || (!p && q)){
            return false;
        }
        else{
            return p->val == q->val && helper(p->left,q->left) && helper(p->right,q->right);
        }
        return false;
    }

    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if(!root){
            return false;
        }
        bool result = helper(root,subRoot);
        return result || isSubtree(root->left,subRoot) || isSubtree(root->right,subRoot);
    }
};