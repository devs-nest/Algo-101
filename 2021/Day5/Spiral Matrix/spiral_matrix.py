class Solution: #CyFun
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        
        while matrix:
            # Add top row
            result.extend(matrix.pop(0))

            # Iterate through new top till 2nd last row while
            # adding last element of row if row is non empty
            for row in matrix[0:-1]:
                if row:
                    result.append(row.pop())
            
            # Add reversed bottom row if exists
            if not matrix:
                break
            result.extend(matrix.pop()[::-1])
            
            # Iterate from new bottom row back up till 2nd row
            # while adding first element from row if row is non empty
            for row in matrix[:0:-1]:
                if row:
                    result.append(row.pop(0))            
        
        return result