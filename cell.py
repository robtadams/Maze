class Cell():

    def __init__(self, cellSize = 10, row = 0, column = 0):

        """ Initialization """

        # Row and Column are used to determine the abstract position of the
        # cell. The first cell should be at (0, 0) while the last cell
        # should be at (N - 1, N - 1) where N is the maximum number of
        # rows and columns in the maze.

        # row: an integer that holds the vertical index of the cell
        self.row = row

        # column: an integer that holds the horizontal index of the cell
        self.column = column

        # X and Y are used to determinme the literal position of the
        # start of the cell on the screen. The cell is an abstract
        # representation of the white box drawn on the screen. This box
        # is used to represent a path, while black boxes represent
        # walls. The X and Y coordinates are used to show where that
        # box should be drawn from.

        # X: an integer that holds the X coordinate of the cell
        self.X = column * cellSize

        # Y: an integer that holds the Y coordinate of the cell
        self.Y = row * cellSize

        # distance: an integer that holds the number of cell's required
        #           to traverse from the start of the maze to this cell
        self.distance = 0

        # isWall: a boolean that keeps track if the cell is a wall or
        #           a path
        self.isWall = True

        # isStart: a boolean that keeps track of the first cell in the maze
        self.isStart = False

        # isEnd: a boolean that keeps track of the end of the maze
        self.isEnd = False

if __name__ == "__main__":

    for i in range(5):

        print("-----")
        print()

        for j in range(5):

            myCell = Cell(row = i, column = j)

            print("Row: {0}\nColumn: {1}\nX: {2}\nY: {3}".format(myCell.row,
                                                                 myCell.column,
                                                                 myCell.X,
                                                                 myCell.Y))
            print()
