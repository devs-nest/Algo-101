class Solution //By CyFun
{
public:
    bool containsDuplicate(vector<int> &nums)
    {
        unordered_set<int> seen;

        for (auto x : nums)
        {
            if (seen.find(x) != seen.end())
            {
                return true;
            }
            seen.insert(x);
        }
        return false;
    }
};