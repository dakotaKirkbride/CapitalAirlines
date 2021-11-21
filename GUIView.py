
from graphics import *
from LoginView import *
from NewUserView import *
from Plane import *
from Manager import *
from Tourist import *
from BusinessTraveler import *
from Family import *
from random import random
from random import randrange


class GUIView:

    # ------------------------------------------------------------------

    def __init__(self):
        """
        Creates GUI window using graphics.py
        """
        self.win = GraphWin("Capital Airlines", 1000, 800)
        self.win.setCoords(0, 0, 100, 80)
        self.win.setBackground("slategrey")

    # ------------------------------------------------------------------

    def drawLoginView(self, plane: Plane, manager: Manager):
        """
        calls loginView class and its methods
        :param plane: selected plane object
        :param manager: selected manager object
        :return: none
        """
        loginView = LoginView(self.win, manager)
        loginView.formatElements()
        loginView.getButton(plane)

    # ------------------------------------------------------------------


def main():

    testPlane = Plane()
    manager = Manager()

    # ||| Uncomment the below line if you'd like for the plane to be randomly filled with passengers
    # VVV Automatically clears the csv prior to generating new passengers to not overfill the plane
    manager.generateRandomPassengers(testPlane, 35, 40)

    # VVV Uncomment this line if you'd like to clear the csv of all passengers
    # manager.clearCSV(testPlane)

    manager.readFromCSV(testPlane)
    guiView = GUIView()
    guiView.drawLoginView(testPlane, manager)


if __name__ == "__main__":
    main()
