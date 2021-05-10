class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent = {v: -1 for v in range(1, len(edges)+1)}

        # ---------------------------------

        def find(u):

            if parent[u] != -1:
                # find root with path compression
                parent[u] = find(parent[u])
                return parent[u]

            else:
                # root node must be with -1
                return u

        # ---------------------------------

        def union(u, v):

            parent_of_u = find(u)
            parent_of_v = find(v)

            if parent_of_u == parent_of_v:

                # u and v has the same parent node
                # this edges froms a cycle in graph
                return True

            else:

                # after adding edge(u, v)
                # graph is still a tree without cycle
                parent[parent_of_u] = parent_of_v
                return False

        # ---------------------------------

        redundant = None
        for u, v in edges:

            if union(u, v):
                # check if edge (u, v) forms a cycle
                redundant = [u, v]
                return redundant
