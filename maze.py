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

        # startRect: a list that contains the startCell's X and Y coordinates
        #           for the maze to render
        startRect = [startCell.X, startCell.Y, self.cellSize, self.cellSize]

        # Draw the start cell on the screen
        pygame.draw.rect(self.screen, "green", startRect)

        pygame.display.update()

        if TEST:
            self.testNum = 0
            print("\n--- BUILD MAZE ---\n")

        self.buildMaze(startCell)

        print("Done :)")

    def buildMaze(self, cell):

        if TEST:
            print("{}. Path".format(self.testNum))
            self.testNum += 1

        self.cellArray[cell.row][cell.column].isWall = False

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

                rand = random.randint(1, len(cell.directions)) - 1

                direction = cell.directions.pop(rand)

            else:

                return

            match direction:

                case "North":

                    if cell.column - 1 >= 0 and not self.cellArray[cell.row - 1][cell.column - 1].isWall:
                        if TEST:
                            print("{}. Case 1 Error: Can't go North".format(self.testNum))
                            print("Path at {0}, {1}\n".format(cell.row - 1, cell.column - 1))

                    elif not self.cellArray[cell.row - 1][cell.column].isWall:
                        if TEST:
                            print("{}. Case 2 Error: Can't go North".format(self.testNum))
                            print("Path at {0}, {1}\n".format(cell.row - 1, cell.column))

                    elif cell.column + 1 < self.width and not self.cellArray[cell.row - 1][cell.column + 1].isWall:
                        if TEST:
                            print("{}. Case 3 Error: Can't go North".format(self.testNum))
                            print("Path at {0}, {1}\n".format(cell.row - 1, cell.column + 1))
                            
                    else:
                        if TEST:
                            print("{}. Heading North".format(self.testNum))
                        self.buildMaze(self.cellArray[cell.row - 1][cell.column])

                case "East":

                    if cell.row - 1 >= 0 and not self.cellArray[cell.row - 1][cell.column + 1].isWall:
                        if TEST:
                            print("{}. Case 4 Error: Can't go East".format(self.testNum))
                            print("Path at {0}, {1}\n".format(cell.row - 1, cell.column + 1))
                        
                    elif not self.cellArray[cell.row][cell.column + 1].isWall:
                        if TEST:
                            print("{}. Case 5 Error: Can't go East".format(self.testNum))
                            print("Path at {0}, {1}\n".format(cell.row, cell.column + 1))

                    elif cell.row + 1 < self.height and not self.cellArray[cell.row + 1][cell.column + 1].isWall:
                        if TEST:
                            print("{}. Case 6 Error: Can't go East".format(self.testNum))
                            print("Path at {0}, {1}\n".format(cell.row + 1, cell.column + 1))
                            
                    else:
                        if TEST:
                            print("{}. Heading East".format(self.testNum))
                        self.buildMaze(self.cellArray[cell.row][cell.column + 1])

                case "South":

                    if cell.column - 1 >= 0 and not self.cellArray[cell.row + 1][cell.column -1].isWall:
                        if TEST:
                            print("{}. Case 7 Error: Can't go South".format(self.testNum))
                            print("Path at {0}, {1}\n".format(cell.row + 1, cell.column - 1))

                    elif not self.cellArray[cell.row + 1][cell.column].isWall:
                        if TEST:
                            print("{}. Case 8 Error: Can't go South".format(self.testNum))
                            print("Path at {0}, {1}\n".format(cell.row + 1, cell.column))

                    elif cell.column + 1 < self.width and not self.cellArray[cell.row + 1][cell.column + 1].isWall:
                        if TEST:
                            print("{}. Case 9 Error: Can't go South".format(self.testNum))
                            print("Path at {0}, {1}\n".format(cell.row + 1, cell.column + 1))
                            
                    else:
                        if TEST:
                            print("{}. Heading South".format(self.testNum))
                        self.buildMaze(self.cellArray[cell.row + 1][cell.column])

                case "West":

                    if cell.row - 1 >= 0 and not self.cellArray[cell.row - 1][cell.column - 1].isWall:
                        if TEST:
                            print("{}. Case 10 Error: Can't go West".format(self.testNum))
                            print("Path at {0}, {1}\n".format(cell.row - 1, cell.column - 1))

                    elif self.cellArray[cell.row][cell.column - 1].isWall:
                        if TEST:
                            print("{}. Case 11 Error: Can't go West".format(self.testNum))
                            print("Path at {0}, {1}\n".format(cell.row, cell.column - 1))

                    elif cell.row + 1 < self.height and not self.cellArray[cell.row + 1][cell.column - 1].isWall:
                        if TEST:
                            print("{}. Case 12 Error: Can't go West".format(self.testNum))
                            print("Path at {0}, {1}\n".format(cell.row + 1, cell.column - 1))

                    else:
                        if TEST:
                            print("{}. Heading West".format(self.testNum))
                        self.buildMaze(self.cellArray[cell.row][cell.column - 1])

        print("{}. Returning".format(self.testNum))      
        return

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
