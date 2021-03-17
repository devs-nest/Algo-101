
import heapq

d = {
    0: [[1, 3], [3, 10]],
    1: [[2, 5], [4, 11]],
    2: [[3, 1], [4, 7]],
    3: [],
    4: []
}

n = 5
distance = [10**9]*n
distance[0] = 0

visited = [False]*n

node = 0
heap = []

heapq.heapify(heap)
heapq.heappush(heap, [distance[node], node])

while(len(heap) > 0):
    node = heapq.heappop(heap)[1]
    
    if visited[node] == True:
        continue
    
    visited[node] = True
    
    for nn, w in d[node]:
        if distance[nn] > distance[node] + w:
            distance[nn] = distance[node] + w
            heapq.heappush(heap, [distance[nn], nn])
            
            
print distance
