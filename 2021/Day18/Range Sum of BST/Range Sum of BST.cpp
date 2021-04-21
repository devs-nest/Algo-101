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
    /*I ll be giving as much details as possible as to what s going on in the recursion stack.
Lets take the binary tree to be [10,5,15,3,7,null,18]
						
						10
						/\
					  5  15
					 /\   \
			       3  7   18
do your inorder traversal as routine
                                                                      sum = 0
                    |   3      |  
                    |   5      |  
                    |   10     |  <-------inorder(root->left)
                    |__________|
                    we reach the NULL condition of the traversal
            as 3 has no left or right nodes a sum of 0 is passed to 3       3    <-
                                                                           /  \    \
                                                                         NULL  NULL 0
           3 is popped out of the stack ans analyzed
                    |          |  3
                    |   5      |  
                    |   10     |  <-------inorder(root->left)
                    |__________|
            but as 3 < 7 (L)
            sum value is not changed                                   sum=0
            then 7 is pushed into the stack
                    |   7      |  
                    |   5      |  
                    |   10     |  <-------inorder(root->right)
                    |__________|
            as 7 has no leaf nodes inorder(root->left) = NULL
                                   sum+=7(as 7 is in the range)       sum=7
                                   inorder(root->right) = NULL
                                   sum=7 is passed to the call stack
                    |          |  7
                    |   5      |  
                    |   10     |  <-------inorder(root->left)
                    |__________|
                Now as both the left and right nodes are visited 5 is analyzed.
                inorder(root->left) = 5
                But since 5 is not in the range sum value doesnt change.
                Now 5 is popped out of the stack.
                    |          |   5   
                    |          |  
                    |   10     |  <-------inorder(root->left)
                    |__________|
                    inorder(rot->right)  continues excecution.
                    |   18     |  
                    |   15     |  
                    |   10     |  <-------inorder(root->right)
                    |__________|
                    18 has no childeren thus sum=7 is passed on to the root.
                    18 is not in the range so sum doesnt change.
                    this process continues and 15 gets added to the sum giving sum=22
                    then 10 gets added  sum=32
                    */
    int sum = 0;
    int inorder(TreeNode *root, int L, int R)
    {
        if (root)
        {
            inorder(root->left, L, R);
            if (root->val >= L && root->val <= R)
                sum += root->val;
            inorder(root->right, L, R);
        }
        return sum;
    }
    int rangeSumBST(TreeNode *root, int L, int R)
    {
        if (!root)
            return 0;
        return inorder(root, L, R);
    }
};