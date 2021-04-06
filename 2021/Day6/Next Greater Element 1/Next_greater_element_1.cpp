class Solution
{
public:
    vector<int> nextGreaterElement(vector<int> &nums1, vector<int> &nums2)
    {
        stack<int> stk;
        unordered_map<int, int> mp;

        for (auto &x : nums2)
        {
            while (!stk.empty() && stk.top() < x)
            {
                mp[stk.top()] = x;
                stk.pop();
            }
            stk.push(x);
        }

        vector<int> ans;
        for (auto &x : nums1)
            ans.push_back(mp.count(x) ? mp[x] : -1);
        return ans;
    }
};