from Array.array2d import Array2D


class Matrix:
    # Creates a matrix of size numRows x numCols initialized to 0
    def __init__(self, numRows, numCols):
        self._theGrid = Array2D(numRows, numCols)
        self._theGrid.clear(0)

    # Return the number of rows in the matrix 
    def numRows(self):
        return self._theGrid.numRows()

    # Returns the number of columns in the matrix
    def numCols(self):
        return self._theGrid.numCols()

    # Return the value of element (i, j) : x[i,j]
    def __getitem__(self, ndxTuple):
        return self._theGrid[ndxTuple[0], ndxTuple[1]]

    # Sets the value of element (i, j) to the value s : x[i,j] = s
    def __setitem__(self, ndxTuple, scalar):
        self._theGrid[ndxTuple[0], ndxTuple[1]] = scalar

    # Scales the matrix by the given scalar.
    def scaleBy(self, scalar):
        for r in self._theGrid.numRows():
            for c in self._theGrid.numCols():
                self[r, c] *= scalar 

    # Creates and returns a new matrix that is the transpose of this matrix
    def transpose(self):
        pass 

    # Creates and returns a new matrix that is the result from matrix addition
    def __add__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and \
            rhsMatrix.numCols() == self.numCols(), \
                "Matrix sizes not compatible for the addition operation"
        newMatrix = Matrix(self.numRows(), self.numCols())
        # Add the corresponding elements in the two matrices 
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r,c] = self[r,c] + rhsMatrix[r,c]
        return newMatrix 

    # Creates and returns a new matrix that is the result from matrix subtraction
    def __sub__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numCols() and \
            rhsMatrix.numCols() == self.numCols(), \
                "Matrix sizes not compatible for the subtraction operation"
        newMatrix = Matrix(self.numRows(), self.numCols())
        # Subtract the corresponding elements in the two matrices 
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r,c] = self[r,c] - newMatrix[r,c]
        return newMatrix

    # Creates and returns a new matrix that is the result from matrix multiplication
    def __mul__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numCols() \
            rhsMatrix.numCols() == self.numRows(), \
                "Matrix sizes not compatible for the multiplication operation"
        newMatrix = Matrix(rhsMatrix.numRows(), rhsMatrix.numCols())

        # for r in self.numRows():
        #     for c in self.numCols():
        #         newMatrix[r,c] = self[r,c] * newMatrix[c,r] + 
        # return newMatrix