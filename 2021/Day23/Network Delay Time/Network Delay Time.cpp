class Solution
{
public:
    // Using Priority queue (Min-heap)
    int networkDelayTime(vector<vector<int>> &times, int N, int K)
    {
        vector<pair<int, int>> g[N + 1];
        for (int i = 0; i < times.size(); i++)
            g[times[i][0]].push_back(make_pair(times[i][1], times[i][2]));
        vector<int> dist(N + 1, 1e9);
        dist[K] = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q;
        q.push(make_pair(0, K));
        pair<int, int> temp;
        bool visit[N + 1];
        memset(visit, false, sizeof(visit));
        while (!q.empty())
        {
            temp = q.top();
            q.pop();
            int u = temp.second;
            visit[u] = true;
            for (int i = 0; i < g[u].size(); i++)
            {
                int v = g[u][i].first;
                int weight = g[u][i].second;
                if (visit[v] == false && dist[v] > dist[u] + weight)
                {
                    dist[v] = dist[u] + weight;
                    q.push(make_pair(dist[v], v));
                }
            }
        }
        int ans = 0;
        for (int i = 1; i < dist.size(); i++)
        {
            ans = max(ans, dist[i]);
        }
        if (ans == 1e9)
            return -1;
        return ans;
    }
};