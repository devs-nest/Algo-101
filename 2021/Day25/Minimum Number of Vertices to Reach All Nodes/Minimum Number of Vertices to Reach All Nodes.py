class Solution:
    def findSmallestSetOfVertices(self, n, A):
        B = set(range(n))
        for x, y in A:
            if y in B:
                B.remove(y)
        return list(B)
