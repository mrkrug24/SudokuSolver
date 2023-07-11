import copy

class SudokuSolver:
    def solve(matrix):
        solution = copy.deepcopy(matrix)
        
        if SudokuSolver.solveHelper(solution):
            return solution
        
        return None

    def solveHelper(solution):
        minPossibleValueCountCell = None
        
        while True:
            minPossibleValueCountCell = None
            
            for rowIndex in range(9):
                for columnIndex in range(9):
                    if solution[rowIndex][columnIndex] != 0:
                        continue
                    
                    possibleValues = SudokuSolver.findPossibleValues(rowIndex, columnIndex, solution)
                    possibleValueCount = len(possibleValues)
                    
                    if possibleValueCount == 0:
                        return False
                    
                    if possibleValueCount == 1:
                        solution[rowIndex][columnIndex] = possibleValues.pop()
                        
                    if not minPossibleValueCountCell or \
                       possibleValueCount < len(minPossibleValueCountCell[1]):
                        minPossibleValueCountCell = ((rowIndex, columnIndex), possibleValues)
                        
            if not minPossibleValueCountCell:
                return True
            
            elif 1 < len( minPossibleValueCountCell[ 1 ] ):
                break
            
        r, c = minPossibleValueCountCell[0]
        
        for v in minPossibleValueCountCell[1]:
            solutionCopy = copy.deepcopy( solution )
            solutionCopy[r][c] = v
            
            if SudokuSolver.solveHelper(solutionCopy):
                for r in range(9):
                    for c in range(9):
                        solution[r][c] = solutionCopy[r][c]
            
                return True
            
        return False

    def findPossibleValues(rowIndex, columnIndex, matrix):
        values = {v for v in range(1, 10)}
        values -= SudokuSolver.getRowValues(rowIndex, matrix)
        values -= SudokuSolver.getColumnValues(columnIndex, matrix)
        values -= SudokuSolver.getBlockValues(rowIndex, columnIndex, matrix)
        return values

    def getRowValues(rowIndex, matrix):
        return set(matrix[rowIndex][:])

    def getColumnValues(columnIndex, matrix):
        return {matrix[r][columnIndex] for r in range(9)}

    def getBlockValues(rowIndex, columnIndex, matrix):
        blockRowStart = 3 * (rowIndex // 3)
        blockColumnStart = 3 * (columnIndex // 3)
        
        return {
            matrix[blockRowStart + r][blockColumnStart + c]
                for r in range(3)
                for c in range(3)
        }

def printMatrix(matrix):
    print("\nAnswer:")
    for row in matrix:
       print(*row)
       
matrix = [[int(j) for j in input().split()] for i in range(9)]
solution = SudokuSolver.solve(matrix)

if solution:
    printMatrix(solution)