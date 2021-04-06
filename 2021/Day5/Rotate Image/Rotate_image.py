class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead. //CyFun
        """

#Transpose
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j],matrix[j][i]= matrix[j][i],matrix[i][j]

#reverse rows
        for row in matrix:
            row.reverse()