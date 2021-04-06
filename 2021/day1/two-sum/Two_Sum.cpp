class Solution //By CyFun
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        map<int, int> hash;
        vector<int> res(2);
        for (int it = 0; it < nums.size(); it++)
        {
            hash[nums[it]] = it;
        }
        for (int i = 0; i < nums.size(); i++)
        {
            int temp = target - nums[i];
            auto a = hash.find(temp);
            if (a != hash.end() && a->second != i)
            {
                res[0] = i;
                res[1] = a->second;
                return res;
            }
        }
        return res;
    }
};