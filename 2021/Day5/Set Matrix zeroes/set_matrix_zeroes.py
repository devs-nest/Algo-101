class Solution: #By CyFun
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        clear_row = False
        clear_col = False
        i = 0
        j = 0
        while j < m:
            if matrix[0][j] == 0:
                clear_row = True
                break
            j += 1
        while i < n:
            if matrix[i][0] == 0:
                clear_col = True
                break
            i += 1
        i = 1
        while i < n:
            j = 1
            while j < m:
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                j += 1
            i += 1
        i = 1
        while i < n:
            if matrix[i][0] == 0:
                j = 1
                while j < m:
                    matrix[i][j] = 0
                    j += 1
            if clear_col:
                matrix[i][0] = 0
            i += 1
        j = 1
        while j < m:
            if matrix[0][j] == 0:
                i = 1
                while i < n:
                    matrix[i][j] = 0
                    i += 1
            if clear_row:
                matrix[0][j] = 0
            j += 1
        if clear_row:
            matrix[0][0] = 0
        if clear_col:
            matrix[0][0] = 0
