#union find

# edges = [[1,2,4], [2,3,5], [3,4,6],[4,2,8] ]


nodes = 4

size = [1]*len(nodes)
link = []
for i in range(len(nodes)):
    link.append(i)
    #   0  1  2  3  4  5  6
link = [0, 0, 0, 0, 3, 5, 6]
size = [5, 1, 1, 2, 1, 1, 1]


def find(i):
    if i == link[i]:
        return i
    return find(link[i])

def merge(i,j): # 2, 3
    i = find(i) # 0
    j = find(j) # 3
    x = size[i] # 3
    y = size[j] # 2

    if x<y:
        i,j = j,i
    
    link[j] = link[i]
    size[i] += size[j]

def same(i,j):
    if find(i) == find(j):
        return True
        

def kruskal():
    edges = [
        [0, 1, 4],
        [1, 3, 6],
        [2, 4, 2],
        [3, 4, 8],
        [5, 6, 4],
        [7, 8, 9],
        [6, 8, 11],
    ]
    edges.sort(key=lambda x:x[2])

    ans = []
    for edge in edges:
        u = edge[0]
        v = edge[1]
        if not same(u,v):
            merge(u,v)
            ans.append(edge)
    
    return ans
        

    
