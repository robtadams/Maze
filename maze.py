import pygame
import random
import time

global TEST
TEST = False

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

        # mazeArray:    a list that contains the coordinates for each cell
        #               in the maze
        self.mazeArray = []

        """ Maze Array Construction """

        # For each row...
        for row in range(self.width):

            # ... build a list for that row
            self.mazeRow = []

            # For each column...
            for column in range(self.height):

                # ... add the coordinates of that cell to mazeRow
                self.mazeRow.append((row * self.cellSize, column * self.cellSize))

                """ Testing """

                # If testing...
                if TEST:

                    # ... if row + column is odd...
                    if (row + column) % 2:

                        # ... construct a rectangle at the cell
                        tempRect = [row * self.cellSize,
                                    column * self.cellSize,
                                    self.cellSize,
                                    self.cellSize]

                        # ... and draw a white rectangle at that cell
                        pygame.draw.rect(self.screen, "white", tempRect)

                        # ... then update the display
                        pygame.display.update()

                        #time.sleep(.1)

            # Then, add the full row to the mazeArray
            self.mazeArray.append(self.mazeRow)

        """ Testing """

        # If testing...
        if TEST:

            # ... for each row in the mazeArray...
            for row in self.mazeArray:

                # ... for each column in the row...
                for column in row:

                    # ... print the coordinate at that cell
                    print(column, end = "")

                print()

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
            time.sleep(0)

myMaze = Maze()
myMaze.main()
