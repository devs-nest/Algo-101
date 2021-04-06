class Solution
{
public:
    void rotate(vector<vector<int>> &matrix)
    {
        int r = matrix.size(), c = matrix[0].size();
        // Transpose Of Matrix        By CyFun
        for (int i = 0; i < r; i++)
        {
            for (int j = 0; j < c; j++)
            {
                if (i <= j)
                {
                    swap(matrix[i][j], matrix[j][i]);
                }
            }
        }
        // Swapping Columns from left to right till half
        for (int i = 0; i < c / 2; i++)
        {
            for (int j = 0; j < r; j++)
            {
                swap(matrix[j][i], matrix[j][r - i - 1]);
            }
        }
    }
};