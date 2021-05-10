class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])

        s = (0, 0)
        d = {}
        d[s] = 0
        h = []
        heapq.heappush(h, [d[s], s])
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                if i == 0 and j == 0:
                    continue
                u = (i, j)
                d[u] = float('inf')
                heapq.heappush(h, [d[u], s])

        while len(h) > 0:
            # route_effort is the maximum abs difference in heights between some pair of
            # directly-connected nodes along the path/route s -> ..-> ... -> u
            route_effort, u = heapq.heappop(h)
            if u == (m - 1, n - 1):
                return route_effort

            for delta in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                v = (u[0] + delta[0], u[1] + delta[1])
                if v[0] < 0 or v[0] == m or v[1] < 0 or v[1] == n:
                    continue
                new_route_effort = max(
                    d[u], abs(heights[u[0]][u[1]] - heights[v[0]][v[1]]))
                if d[v] > new_route_effort:
                    d[v] = new_route_effort
                    heapq.heappush(h, [d[v], v])

        return 0
