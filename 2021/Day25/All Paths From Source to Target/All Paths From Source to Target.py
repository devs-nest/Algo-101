class Solution:
    def allPathsSourceTarget(self, graph):
        def dfs(formed):
            if formed[-1] == n - 1:
                sol.append(formed)
                return
            for child in graph[formed[-1]]:
                dfs(formed + [child])

        sol, n = [], len(graph)
        dfs([0])
        return sol
