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
class Solution
{
public:
    TreeNode *bstToGst(TreeNode *root)
    {
        int acc_sum = 0;
        sum_node(root, acc_sum);
        return root;
    }

    void sum_node(TreeNode *node, int &acc_sum)
    {
        if (node == NULL)
            return;
        sum_node(node->right, acc_sum);
        node->val += acc_sum;
        acc_sum = node->val;
        sum_node(node->left, acc_sum);
    }
};