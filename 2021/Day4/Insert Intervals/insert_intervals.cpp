class Solution//By CyFun
{
public:
    vector<vector<int>> insert(vector<vector<int>> &v1, vector<int> &v2)
    {
        if (!v1.size())
        {
            v1.push_back(v2);
            return v1;
        }
        v1.push_back(v2);
        sort(v1.begin(), v1.end());
        stack<pair<int, int>> s;
        s.push({v1[0][0], v1[0][1]});
        for (int i = 1; i < v1.size(); i++)
        {
            int a = s.top().second;
            int b = v1[i][0];
            if (a >= b && a <= v1[i][1])
            {
                s.top().second = v1[i][1];
            }
            else if (a < b)
            {
                s.push({v1[i][0], v1[i][1]});
            }
        }
        vector<vector<int>> v;
        while (s.size() > 0)
        {
            vector<int> v3;
            v3.push_back(s.top().first);
            v3.push_back(s.top().second);
            v.push_back(v3);
            s.pop();
        }
        reverse(v.begin(), v.end());
        return v;
    }
};