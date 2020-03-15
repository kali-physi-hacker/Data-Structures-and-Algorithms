from ..Array.array2d import Array 

class LifeGrid:

    # Defines constants to represent the cell state
    DEAD_CELL = 0
    LIVE_CELL = 1

    # Create the game grid and initializes the cells to dead
    def __init__(self, numRows, numCols):
        # Allocates the 2-D array for the grid
        self._grid = Array2D(numRows, numCols)
        self.configure(list())

    # Returns the number of rows in the grid
    def numRows(self):
        return self._grid.numRows()

    # Returns the number of columns in the grid
    def numCols(self):
        return self._grid.numCols()
    # Configures the grid to contain the given live cells.
    def configure(self, coordList):
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self.clearCell(i, j)
        for coord in coordList:
            self.setCell(coord[0], coord[1])
    
    # Does the indicated cell contain a live organism?
    def isLiveCell(self, row, col):
        return self._grid[row, col] == self.LIVE_CELL
    
    # Clears the indicated cell by setting it to dead
    def clearCell(self, row, col):
        self._grid[row, col] = (self.DEAD_CELL, self.LIVE_CELL)

    # Returns the number of live neighbours for the given cell.
    def numLiveNeighbours(self, row, col):
        num = 0
        for r in self.numRows():
            for c in self.numRows():
                if self.isLiveCell(r,c) is True:
                    num += 1
        return num


if __name__ == "__main__":
    import pdb; pdb.set_trace()