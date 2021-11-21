
from typing import List


class Plane:

    # ------------------------------------------------------------------

    def __init__(self):
        """
        plane constructor method
        """
        self.rows = 20
        self.seatsPerRow = 6
        self.totalSeats = self.rows * self.seatsPerRow
        self.seatsBooked = 0
        self.seatsLeft = self.totalSeats - self.seatsBooked
        # will hold int values indicating what passenger type is sitting in each seat
        #   0 = Empty seat
        #   1 = Business traveler
        #   2 = Tourist traveler
        #   3 = Family traveler
        self.planeMatrix = [0] * self.totalSeats
        # number of passenger groups that have booked tickets
        self.passengerGroupNums = 0
        # dictionary that holds a passenger object (Bus traveler, Tourist, or Family) as the key
        # with their respective satisfaction level as the value
        self.passengerGroups = {}
        # stores login info of passengers. Usernames are the keys and passwords are the values
        self.passengerAccounts = {}

    # ------------------------------------------------------------------

    def printMatrix(self):
        """
        Prints plane matrix to terminal
        :return: plane matrix in terminal
        """
        seatIndex = 0

        print("FRONT OF PLANE", "\n")

        for i in range(self.rows):
            for j in range(self.seatsPerRow):
                if self.planeMatrix[seatIndex] == 0:
                    if j == 2:
                        print("x  ", end='')
                    else:
                        print("x ", end='')
                else:
                    if j == 2:
                        print("✓  ", end='')
                    else:
                        print("✓ ", end='')
                seatIndex += 1
            print(end="\n")
        print(end="\n")
        print("BACK OF PLANE")
        print(end="\n")
        print("Seats Booked: ", self.seatsBooked, end="\n")
        print("Seats Remaining: ", self.seatsLeft, end="\n")

    # ------------------------------------------------------------------











