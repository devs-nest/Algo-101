1. Minimum Spanning Tree.
2. DSU
3. How to construct a MST using Kruskal Algorithm


1. MST

graph -> G
MST OF g WILL BE the tree[ aka a graph without cycle] whose sum of weight of edge is minimum.
DSU->
Graph G -> there will be certain vertices which will be completly connected to each other and there will be certain
vertices A and B which are not connected, in this scenario we end up with two connected sets in which intersection
of set A and set B is Null

These sets are disjoint sets!

Kruskal Algorithm
Agenda: Kruskal Algorithm is used to construct and MST greedily.
1. Sort all edges in increasing order ( or non -decreasing order).
2. Pick edges, and see if we can connected the edge without reaching a cycle.
3. We connect it if we are not reaching a cycle and that's it.

When we stop? When connected edges are V-1, where V is the total number of vertices.

1. Sorting
2. Where we need to figure out if there is a cycle or not ?
    this leads to another problem where we need to find if there exists a cycle or not in a graph?

    1. How we detect a cycle?
        - we do a traversal, and we see if we are encountering any previously visited edge or not?

 T, C ->  O(N log M) + N*M
 How to figure out how many disjoint sets exists in a graph?
a <-> b <-> c <-> d <-> e  f<->g
if root is c:

 - while all nodes are not visited:
    dfs()
    count++