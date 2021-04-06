class Solution
{
public:
    vector<int> productExceptSelf(vector<int> &nums)
    {
        vector<int> left(nums.size(), 1);
        vector<int> right(nums.size(), 1);
        int n = nums.size();

        for (int i = 1; i < nums.size(); i++)
        {
            left[i] = left[i - 1] * nums[i - 1];
            right[n - 1 - i] = right[n - 1 - i + 1] * nums[n - 1 - i + 1];
        }
        for (int i = 0; i < nums.size(); i++)
        {
            right[i] *= left[i];
        }
        return right;
    }
};