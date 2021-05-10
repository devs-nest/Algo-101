class Solution
{
public:
    vector<int> parent;
    vector<int> findRedundantConnection(vector<vector<int>> &edges)
    {
        if (edges.size() == 0)
            return {};
        parent.resize(edges.size() + 1);
        for (int i = 1; i < edges.size() + 1; i++)
        {
            parent[i] = i;
        }
        for (vector<int> edge : edges)
        {
            int f1 = find(edge[0]);
            int f2 = find(edge[1]);
            if (f1 != f2)
                parent[f1] = f2;
            else
                return edge;
        }
        return {};
    }
    int find(int x)
    {
        return parent[x] == x ? x : find(parent[x]);
    }
};