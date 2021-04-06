class Solution //By CyFun
{
public:
    int maxSubArray(vector<int> &nums)
    {
        int cur = nums[0];
        int maxv = cur;
        for (int i = 1; i < nums.size(); i++)
        {
            cur = cur + nums[i] > nums[i] ? cur + nums[i] : nums[i];
            maxv = max(maxv, cur);
        }
        return maxv;
    }
};