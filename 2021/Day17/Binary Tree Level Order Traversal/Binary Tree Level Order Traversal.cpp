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
    vector<vector<int>> levelOrder(TreeNode *root)
    {

        // Early return condition.
        if (!root)
            return {};

        vector<vector<int>> ourRes; // Carries our result
        vector<int> singleIter;     // Carries a single iteration
                                    // Store the node pointers for the most flexibility.
        queue<TreeNode *> ourNodes;

        // Seed with initial root value.
        ourNodes.push(root);

        while (!ourNodes.empty())
        {
            // Get the size of the current level
            int size = ourNodes.size();

            // Work on the current level.
            while (size--)
            {
                // Push all nodes for a given level into the singleIter vector
                TreeNode *topElement = ourNodes.front();
                singleIter.push_back(topElement->val);
                ourNodes.pop();
                // Prime their children for the next iteration (put all their children in the queue, if they exist).
                if (topElement->left)
                    ourNodes.push(topElement->left);
                if (topElement->right)
                    ourNodes.push(topElement->right);
            }
            // Store all the nodes of one level in a single grouping and push them into our result
            ourRes.push_back(singleIter);
            // Clear the group for the next iteration.
            singleIter.clear();
        }

        return ourRes;
    }
};