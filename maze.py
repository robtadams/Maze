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
        for row in range(self.width):
            
            # ... build a list for each cell in that row
            self.cellRow = []

            # For each column...
            for column in range(self.height):

                # ... create a new cell
                newCell = Cell(row = row, column = column)
                
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

                        time.sleep(.025)

            # Then, add the full row to the mazeArray
            self.cellArray.append(self.cellRow)

            if TEST:

                print("----------")

        """ Noise """

        if NOISE:

            self.randomPrint()

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

myMaze = Maze()
myMaze.main()
