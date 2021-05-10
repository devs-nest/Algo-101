class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        graph = collections.defaultdict(dict)
        
        for frm, to, cost in times:
            graph[frm][to] = cost
        
        distances = { i: float("inf") for i in range(1, N+1)}
        distances[K] = 0
        min_dist = [(0,K)]
        visited = set()

        while min_dist:
            
            cur_dist, cur = heapq.heappop(min_dist)
            if cur in visited: continue
            visited.add(cur)    
            
            for neighbor in graph[cur]:
                if neighbor in visited: continue
                this_dist = cur_dist + graph[cur][neighbor]
                if this_dist  < distances[neighbor]:
                    distances[neighbor] = this_dist
                    heapq.heappush(min_dist, (this_dist, neighbor))
            
        if len(visited) != len(distances): return -1
        return distances[max(distances,key=distances.get)]