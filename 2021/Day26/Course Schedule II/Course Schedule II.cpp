class Solution
{
public:
    bool dfs(int node, vector<vector<int>> &graph, vector<int> &visited, vector<int> &result)
    {
        visited[node] = 1;
        for (int i = 0; i < graph[node].size(); i++)
        {
            if (visited[graph[node][i]] == 1)
                return false; // if this node is unexplored that means there is a cycle
            if (visited[graph[node][i]] == 0)
            {
                if (!dfs(graph[node][i], graph, visited, result)) //return false
                    return false;
            }
        }
        visited[node] = 2;      //if function comes till here then we can mark the current node as 2 i.e, visited
        result.push_back(node); //we will push the visited nodes to the resulting array
        return true;
    }
    vector<int> findOrder(int numCourses, vector<vector<int>> &prerequisites)
    {
        vector<vector<int>> graph(numCourses);
        for (int i = 0; i < prerequisites.size(); i++)
        {
            graph[prerequisites[i][0]].push_back(prerequisites[i][1]); //making an adjacency list
        }
        vector<int> visited(numCourses, 0); //for keeping track of the nodes position.
                                            //We first initialize every node as 0 i,e. unvisited
        vector<int> result;                 //result vector
        bool flag = true;
        for (int i = 0; i < numCourses; i++)
        {
            if (visited[i] == 0)
            {
                if (!dfs(i, graph, visited, result))
                {
                    flag = false; // it will return false if there is a cycle detected so we can break it
                    break;
                }
            }
        }
        if (!flag)
            return vector<int>();
        return result;
    }
};