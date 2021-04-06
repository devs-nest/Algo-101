class Solution//By CyFun
{
public:
    vector<vector<int>> merge(vector<vector<int>> &a)
    {
        if (a.size() == 1)
            return a;
        sort(a.begin(), a.end(), [](const vector<int> &v1, const vector<int> &v2) { return v1[0] < v2[0]; });

        vector<vector<int>> res;

        for (int i = 1; i < a.size(); i++)
        {
            if (a[i][0] <= a[i - 1][1])
            {
                a[i][0] = a[i - 1][0];
                a[i][1] = max(a[i][1], a[i - 1][1]);

                if (i == a.size() - 1)
                    res.push_back(a[i]);
            }
            else
            {
                res.push_back(a[i - 1]);

                if (i == a.size() - 1)
                    res.push_back(a[i]);
            }
        }

        return res;
    }
};