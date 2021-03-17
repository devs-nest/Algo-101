
import heapq
d = {
    1: [[2,12], [3,19]],
    2: [[1,12],[3,16], [4,11]],
    3: [[1,19],[2,16], [5, 14]],
    4: [[2,11],[5,25]],
    5: [[4,25],[3,14]]
}


h = [] 
heapq.heapify(h)

h = []

V= [1,2,3,4,5]
X = set()
result = []
n = V[0] # first node
X.add(n)

for edge in d[n]:
    node, weight = edge
    heapq.heappush(h, [weight, node, n])

while(len(X) != len(V)):
    weight, n, st = heapq.heappop(h)
    if n in X:
        continue
    X.add(n)
    result.append([st, n, weight])
    for edge in d[n]:
        node, weight = edge
        if node not in X:
            heapq.heappush(h, [weight, node, n])

print (result)
    
    






