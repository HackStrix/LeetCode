/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


struct TreeNode* invertTree(struct TreeNode* root){
    if (root == NULL) return root;
    struct TreeNode *tLeft = root->left;
    root->left = root->right;
    invertTree(root->right);
    invertTree(tLeft);
    root->right = tLeft;
    return root;
}