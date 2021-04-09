class Solution
{
public:
    vector<vector<string>> groupAnagrams(vector<string> &strs)
    {

        vector<vector<string>> ans;
        int ptr = 1;
        unordered_map<string, int> mp;

        for (string s : strs)
        {
            string d = s;
            sort(d.begin(), d.end());

            if (mp[d] == 0)
            {
                mp[d] = ptr++;
            }

            if (ans.size() == mp[d] - 1)
            {
                ans.push_back(vector<string>());
            }

            ans[mp[d] - 1].push_back(s);
        }
        return ans;
    }
};