class Solution
{
public:
    int search(vector<int> &nums, int target)
    {
        int n = nums.size();
        int ans;
        bool found = false;
        for (int i = 0; i < n; i++)
        {
            if (nums[i] == target)
            {
                ans = i;
                found = true;
            }
        }
        if (found == false)
        {
            return -1;
        }
        return ans;
    }
};