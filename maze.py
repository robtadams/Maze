import pygame
import random
import time
from cell import Cell

global TEST
TEST = True

global NOISE
NOISE = False

class Maze():

    def __init__(self):
        
        """ Initialization """

        # Initializes Pygame
        pygame.init()

        """ Default Construction """

        # width:    an integer the holds the number of cells wide the maze
        #           will be
        self.width = 50

        # height:   an integer that holds the number of cells tall the maze
        #           will be
        self.height = 40

        # cellSize: an integer that holds the number of pixels tall/wide
        #           each cell will be
        self.cellSize = 10

        # screen:   a Pygame window that is width * cellSize wide,
        #           and height * cellSize tall
        self.screen = pygame.display.set_mode((self.width * self.cellSize,
                                              self.height * self.cellSize))

        # endCell: the path cell furthest from the start cell
        self.endCell = None

    def main(self):

        # cellArray:    a list that contains the logic for each cell in the maze
        self.cellArray = []

        """ Cell Array Construction """

        if TEST:

            print("\n--- CELL ARRAY TEST ---\n")

        # For each row...
        for row in range(self.height):
            
            # ... build a list for each cell in that row
            self.cellRow = []

            # For each column...
            for column in range(self.width):

                # ... create a new cell
                newCell = Cell(row = row, column = column)

                if newCell.row == 0:
                    newCell.directions.remove("North")

                if newCell.row == self.height - 1:
                    newCell.directions.remove("South")

                if newCell.column == 0:
                    newCell.directions.remove("West")

                if newCell.column == self.width - 1:
                    newCell.directions.remove("East")
                
                # ... add the cell to cellRow
                self.cellRow.append(newCell)

                """ Testing """

                # If testing...
                if TEST:

                    print("[{0}, {1}] : ({2}, {3})".format(newCell.row,
                                                          newCell.column,
                                                          newCell.X,
                                                          newCell.Y))
                    
                    # ... if row + column is odd...
                    if (row + column) % 2:

                        # ... construct a rectangle at the cell
                        tempRect = [newCell.X,
                                    newCell.Y,
                                    self.cellSize,
                                    self.cellSize]

                        # ... and draw a white rectangle at that cell
                        pygame.draw.rect(self.screen, "white", tempRect)

                        # ... then update the display
                        pygame.display.update()

                        #time.sleep(.025)

            # Then, add the full row to the mazeArray
            self.cellArray.append(self.cellRow)

            if TEST:

                print("----------")

        if TEST:

            time.sleep(1)
            
            self.screen.fill("black")

            pygame.display.update()

        """ Maze Building """

        self.startMaze()

    def startMaze(self):

        # randStart: an integer that holds the starting height for the first
        #           path cell in the maze
        randStart = random.randint(1, self.height - 2)

        # startCell: the first path cell in the maze
        startCell = self.cellArray[randStart][0]

        # The startCell is the beginning of the maze
        startCell.isStart = True

        # Initialize the endCell to the first cell in the maze
        self.endCell = startCell

        # startRect: a list that contains the startCell's X and Y coordinates
        #           for the maze to render
        startRect = [startCell.X, startCell.Y, self.cellSize, self.cellSize]

        # Draw the start cell on the screen
        pygame.draw.rect(self.screen, "green", startRect)

        # Update the screen
        pygame.display.update()

        if TEST:
            self.testNum = 0
            print("\n--- BUILD MAZE ---\n")

        # Begin building the maze at startCell
        self.buildMaze(startCell)

        endRect = [self.endCell.X, self.endCell.Y, self.cellSize, self.cellSize]

        pygame.draw.rect(self.screen, "red", endRect)

        pygame.display.update()

        print("Done :)")

        time.sleep(10)

        pygame.quit()

    def buildMaze(self, cell):

        if TEST:
            print("{}. Path".format(self.testNum))
            self.testNum += 1

        cell.isWall = False

        if cell.distance > self.endCell.distance:
            self.endCell = cell

        pathRect = [cell.X, cell.Y, self.cellSize, self.cellSize]

        if self.screen.get_at((cell.X, cell.Y)) == (0, 0, 0, 255):
            pygame.draw.rect(self.screen, "white", pathRect)
            if TEST:
                print("{}. Built".format(self.testNum))

        else:
            pygame.draw.rect(self.screen, "red", pathRect)
            if TEST:
                print("{}. Overwrite")
                print("{0}, {1}\n".format(cell.row, cell.column))

        pygame.display.update()

        for i in range(len(cell.directions)):

            if len(cell.directions) > 0:

                rand = random.randint(0, len(cell.directions) - 1)

                direction = cell.directions.pop(rand)

            else:

                return

            match direction:

                case "North":
                    
                    if self.checkNorth(cell):
                        if TEST:
                            print("{}. Heading North".format(self.testNum))
                            
                        self.buildMaze(self.cellArray[cell.row - 1][cell.column])

                case "East":

                    if self.checkEast(cell):
                        if TEST:
                            print("{}. Heading East".format(self.testNum))
                        self.buildMaze(self.cellArray[cell.row][cell.column + 1])

                case "South":
       
                    if self.checkSouth(cell):
                        if TEST:
                            print("{}. Heading South".format(self.testNum))
                        self.buildMaze(self.cellArray[cell.row + 1][cell.column])

                case "West":
                    
                    if self.checkWest(cell):
                        if TEST:
                            print("{}. Heading West".format(self.testNum))
                        self.buildMaze(self.cellArray[cell.row][cell.column - 1])

        print("{}. Returning".format(self.testNum))      
        return

    def checkNorth(self, cell):
        
        # Check the cells in the adjacent rows...
        for rowMod in (-2, -1):

            # ... check the cells in the adjacent columns...
            for colMod in (-1, 0, 1):

                # newRow: the Y coordinate for the adjacent cell
                newRow = cell.row + rowMod

                # newCol: the X coordinate for the adjacent cell
                newCol = cell.column + colMod

                # ... if the cell is in bounds...
                if newRow >= 0:
                    if newCol >= 0 and newCol < self.width:

                        # ... get the adjacent cell...
                        checkCell = self.cellArray[newRow][newCol]

                        # ... if that cell is not a wall...
                        if not checkCell.isWall:

                            # ... then don't build in that direction
                            return False

        cell.distance = self.cellArray[cell.row - 1][cell.column].distance + 1

        # If all adjacent cells are walls, then you may build in that direction
        return True

    def checkEast(self, cell):

        for rowMod in (-1, 0, 1):

            for colMod in (1, 2):

                newRow = cell.row + rowMod

                newCol = cell.column + colMod

                if newRow >= 0 and newRow < self.height:

                    if newCol < self.width:

                        checkCell = self.cellArray[newRow][newCol]

                        if not checkCell.isWall:

                            return False

        cell.distance = self.cellArray[cell.row][cell.column + 1].distance + 1

        return True

    def checkSouth(self, cell):

        for rowMod in (1, 2):

            for colMod in (-1, 0, 1):

                newRow = cell.row + rowMod

                newCol = cell.column + colMod

                if newRow < self.height:

                    if newCol >= 0 and newCol < self.width:

                        checkCell = self.cellArray[newRow][newCol]

                        if not checkCell.isWall:

                            return False

        cell.distance = self.cellArray[cell.row + 1][cell.column].distance + 1
        
        return True

    def checkWest(self, cell):

        for rowMod in (-1, 0, 1):

            for colMod in (-2, -1):

                newRow = cell.row + rowMod

                newCol = cell.column + colMod

                if newRow >= 0 and newRow < self.height:

                    if newCol >= 0:

                        checkCell = self.cellArray[newRow][newCol]

                        if not checkCell.isWall:

                            return False

        cell.distance = self.cellArray[cell.row][cell.column - 1].distance + 1

        return True


    def randomPrint(self):

        """ Random Printing """

        # Loop forever...
        while True:

            # ... fill the screen with black pixels
            self.screen.fill("black")

            # For each row in mazeArray...
            for i, row in enumerate(self.mazeArray):

                # ... for each column in the row...
                for j, column in enumerate(row):

                    # Generate a random integer, if it's 1...
                    if random.randint(0, 1):

                        # ... construct a rectangle at the cell
                        # Note: column is the X-axis, and row is the Y-axis
                        tempRect = [column * self.cellSize,
                                    row * self.cellSize,
                                    self.cellSize,
                                    self.cellSize]

                        # ... and draw a white rectangle at that cell
                        pygame.draw.rect(self.screen, "white", (i * self.cellSize,
                                                                j * self.cellSize,
                                                                self.cellSize,
                                                                self.cellSize))

            # ... then update the display
            pygame.display.update()

            # Wait so the user can see the maze generation
            time.sleep(1)

if __name__ == "__main__":

    myMaze = Maze()
    myMaze.main()
