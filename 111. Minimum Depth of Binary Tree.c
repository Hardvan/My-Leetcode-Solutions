/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int minDepth(struct TreeNode* root){
    if (root == NULL)
        return 0;
    
    int d_left = minDepth(root->left);
    int d_right = minDepth(root->right);

    if (d_left == 0 || d_right == 0)
        return d_left + d_right + 1;

    if(d_left <= d_right)
        return d_left + 1;
    else
        return d_right + 1;
}
