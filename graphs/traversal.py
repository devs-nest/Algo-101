#N M
N is total the number of vertices and M is total number of edges
M lines,
a b

a -> b
a <- b

1,2,3,4,5
N 5
M 7

1 2
2 3
3 4
4 5
2 4
2 5
1 5

How to store graph?

graph[N][N];

for i in range(0, M):

    graph[b].push(a)
    graph[a].push(b)


1 2 5
2 1 3 4 5
3 2 4
4 2 3 5
5 1 2 4

1.4
2. 5 3 2
3. 1 3 2

5. 5

    4

1   2    5



How to write dfs

visited = {};

1. Pick any node
2. push it into stack
3. keep reading the stack's top element
4. for the top element visit it's graph array
5. if the nodes are not visited mark them visited and push them into stack.

def dfs():
    stack<int>s;
    s.push(4);
    while  stack is not empty :
        current_node = s.top()
        s.pop()
        for i in range(graph[current_node]):
            connected_node = graph[current_node][i];
            if !visited[connected_node]:
                s.push(connected_node)

    def bfs():
        queue < int > s;
        q.push(4);
        while queue is not empty:
            current_node = q.top()
            s.pop()
            for i in range(graph[current_node]):
                connected_node = graph[current_node][i];
                if !visited[connected_node]:
                    q.push(connected_node)

