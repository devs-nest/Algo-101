class Solution
{
private:
    void dfs(const vector<vector<int>> &matrix, const vector<pair<int, int>> &coords, vector<vector<bool>> &visited, int i, int j)
    {
        visited[i][j] = true;

        for (auto &coord : coords)
        {
            int next_i = coord.first + i;
            int next_j = coord.second + j;

            // since we're going backwards (from "ocean" instead of to) we want the next node's value to be equal to or more than the current node's value
            if (is_in_bounds(matrix, next_i, next_j) && !visited[next_i][next_j] && matrix[next_i][next_j] >= matrix[i][j])
            {
                dfs(matrix, coords, visited, next_i, next_j);
            }
        }
    }

    bool is_in_bounds(const vector<vector<int>> &matrix, int i, int j)
    {
        return i >= 0 && j >= 0 && i < matrix.size() && j < matrix[0].size();
    }

public:
    vector<vector<int>> pacificAtlantic(const vector<vector<int>> &matrix)
    {
        if (matrix.empty())
            return vector<vector<int>>();

        const vector<pair<int, int>> coords = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};

        int n = matrix.size(), m = matrix[0].size();
        vector<vector<bool>> visited_atlantic(n, vector<bool>(m, false));
        vector<vector<bool>> visited_pacific(n, vector<bool>(m, false));

        for (int i = 0; i < n; i++)
        {
            // left edge for pacific ocean
            dfs(matrix, coords, visited_pacific, i, 0);
            // right edge for atlantic ocean
            dfs(matrix, coords, visited_atlantic, i, m - 1);
        }
        for (int j = 0; j < m; j++)
        {
            // top edge for pacific ocean
            dfs(matrix, coords, visited_pacific, 0, j);
            // bottom edge for atlantic ocean
            dfs(matrix, coords, visited_atlantic, n - 1, j);
        }

        vector<vector<int>> result;
        // find the nodes that can reach both oceans
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (visited_pacific[i][j] && visited_atlantic[i][j])
                    result.push_back({i, j});

        return result;
    }
};
