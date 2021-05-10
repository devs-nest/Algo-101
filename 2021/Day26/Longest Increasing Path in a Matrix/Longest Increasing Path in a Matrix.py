class Solution:
    def longestIncreasingPath(self, matrix):
        # idea, use topological sort, search around to find the # of incoming nodes, start with zero indegree with queue, pop from queue, search around and reduce the indegree by 1; push to queue if indegree is 0. output the steps. Time O(mn) and Space O(mn).
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        hmap = {}
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                cnt = 0
                for dx, dy in directions:
                    x = i + dx
                    y = j + dy
                    if 0 <= x <= m-1 and 0 <= y <= n-1 and matrix[x][y] < matrix[i][j]:
                        cnt += 1
                hmap[(i, j)] = cnt  # map point to the # of incoming degree
                if cnt == 0:
                    queue.append((i, j))  # append point (i,j) to queue
        # bfs with queue, and update the step until queue is empty
        step = 0
        while queue:
            size = len(queue)
            for k in range(size):
                i, j = queue.popleft()
                for dx, dy in directions:
                    x = i + dx
                    y = j + dy
                    if 0 <= x <= m-1 and 0 <= y <= n-1 and matrix[x][y] > matrix[i][j] and (x, y) in hmap:
                        hmap[(x, y)] -= 1
                        if hmap[(x, y)] == 0:
                            queue.append((x, y))
            step += 1
        return step
