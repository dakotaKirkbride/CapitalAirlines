

from graphics import *
from button import *
from Plane import *
from Manager import *
from NewUserView import *
from Tourist import *
from BusinessTraveler import *
from Family import *
from TicketView import *


class CategorySelectionView:

    # ------------------------------------------------------------------

    def __init__(self, win: GraphWin, username: str, password: str, plane: Plane, manager: Manager):
        """
        Category Selction View in which user chooses passenger type and any preferences that might come with
        :param win: selected graphics window
        :param username: username of account entered in previous view
        :param password: password of account entered in previous view
        :param plane: selected plane object
        :param manager: selected manager object
        """
        self.win = win
        self.plane = plane
        self.manager = manager
        self.username = username
        self.password = password
        self.allViewElements = []
        self.preferenceElements = []
        self.welcomeText = Text(Point(20, 65), f"Welcome, {username}!")
        self.specifierText = Text(Point(26, 55), "Please select your passenger type")
        self.busTravelerButton = None
        self.touristButton = None
        self.familyButton = None
        self.quitButton = None

    # ------------------------------------------------------------------

    def formatElements(self):
        """
        Formats/Draws the elements of the view
        """

        self.welcomeText.setSize(30)
        self.welcomeText.setFace("courier")
        self.welcomeText.draw(self.win)
        self.allViewElements.append(self.welcomeText)

        self.specifierText.setSize(16)
        self.specifierText.setFace("courier")
        self.specifierText.setStyle("bold")
        self.specifierText.draw(self.win)
        self.allViewElements.append(self.specifierText)

        self.busTravelerButton = Button(self.win, Point(15, 50), 12, 4, "Business Traveler")
        self.busTravelerButton.activate()
        self.allViewElements.append(self.busTravelerButton)

        self.touristButton = Button(self.win, Point(30, 50), 12, 4, "Tourist")
        self.touristButton.activate()
        self.allViewElements.append(self.touristButton)

        self.familyButton = Button(self.win, Point(45, 50), 12, 4, "Family")
        self.familyButton.activate()
        self.allViewElements.append(self.familyButton)

        self.quitButton = Button(self.win, Point(90, 10), 10, 5, "Quit")
        self.quitButton.activate()
        self.allViewElements.append(self.quitButton)

    # ------------------------------------------------------------------

    def getButton(self):
        """
        Checks if any of the drawn buttons have been clicked, calls respective function if so
        """
        while True:
            p = self.win.getMouse()

            if self.quitButton.clicked(p):
                exit(0)
            if self.busTravelerButton.clicked(p):
                self.checkBusPref1()
                break
            if self.touristButton.clicked(p):
                self.checkTouristPreferences()
                break
            if self.familyButton.clicked(p):
                self.checkFamilyPreferences()
                break

    # ------------------------------------------------------------------

    def checkBusPref1(self):
        """
        Draws row of buttons for business passenger to select Business Select preference
        Checks all other buttons for click
        calls checkBusPref2 if one of the business preference buttons have been clicked
        """
        for i in self.preferenceElements:
            i.undraw()
        self.preferenceElements.clear()

        preferenceText = Text(Point(24, 45), "Please select your preferences")
        preferenceText.setStyle("bold")
        preferenceText.setSize(16)
        preferenceText.setFace("courier")
        preferenceText.draw(self.win)
        self.preferenceElements.append(preferenceText)

        busSelectPreference = Text(Point(16, 42), "Row Preference")
        busSelectPreference.setFace("courier")
        busSelectPreference.draw(self.win)
        self.preferenceElements.append(busSelectPreference)

        busSelectButton = Button(self.win, Point(15, 38), 12, 4, "Business Select")
        busSelectButton.activate()
        self.preferenceElements.append(busSelectButton)

        noBusSelectButton = Button(self.win, Point(30, 38), 12, 4, "Regular Seating")
        noBusSelectButton.activate()
        self.preferenceElements.append(noBusSelectButton)

        while True:
            p2 = self.win.getMouse()

            if self.quitButton.clicked(p2):
                exit(0)
            elif busSelectButton.clicked(p2):
                preferBusinessSelect = True
                self.checkBusPref2(preferBusinessSelect)
                break
            elif noBusSelectButton.clicked(p2):
                preferBusinessSelect = False
                self.checkBusPref2(preferBusinessSelect)
                break
            elif self.touristButton.clicked(p2):
                self.checkTouristPreferences()
                break
            elif self.familyButton.clicked(p2):
                self.checkFamilyPreferences()
                break

    # ------------------------------------------------------------------

    def checkBusPref2(self, preferBusinessSelect: bool):
        """
        Called after one of the row 1 business preference buttons have been clicked
        Calls checkBusPref3 if row 2 button clicked
        :param preferBusinessSelect: Result of which first row button is clicked
        """
        seatPreferenceText = Text(Point(17, 32), "Seating Preference")
        seatPreferenceText.setFace("courier")
        seatPreferenceText.draw(self.win)
        self.preferenceElements.append(seatPreferenceText)

        windowPreferenceButton = Button(self.win, Point(13, 28), 8, 4, "Window")
        windowPreferenceButton.activate()
        self.preferenceElements.append(windowPreferenceButton)

        aislePreferenceButton = Button(self.win, Point(24, 28), 8, 4, "Aisle")
        aislePreferenceButton.activate()
        self.preferenceElements.append(aislePreferenceButton)

        noPreferenceButton = Button(self.win, Point(35, 28), 8, 4, "None")
        noPreferenceButton.activate()
        self.preferenceElements.append(noPreferenceButton)

        while True:
            p3 = self.win.getMouse()

            if self.quitButton.clicked(p3):
                exit(0)
            elif windowPreferenceButton.clicked(p3):
                seatPreference = "Window"
                self.checkBusPref3(preferBusinessSelect, seatPreference)
                break
            elif aislePreferenceButton.clicked(p3):
                seatPreference = "Aisle"
                self.checkBusPref3(preferBusinessSelect, seatPreference)
                break
            elif noPreferenceButton.clicked(p3):
                seatPreference = "None"
                self.checkBusPref3(preferBusinessSelect, seatPreference)
                break
            elif self.touristButton.clicked(p3):
                self.checkTouristPreferences()
                break
            elif self.familyButton.clicked(p3):
                self.checkFamilyPreferences()
                break

    # ------------------------------------------------------------------

    def checkBusPref3(self, preferBusinessSelect: bool, seatPreference: str):
        """
       Called after one of the row 2 business preference buttons have been clicked
       Draw submit button
       Calls Ticket view if submitButton is clicked
       :param preferBusinessSelect: Result of which first row button is clicked
       :param seatPreference: Result of which second row button is clicked
       """
        submitButton = Button(self.win, Point(25, 20), 12, 4, "Book Tickets")
        submitButton.rect.setFill(color_rgb(204, 107, 91))
        submitButton.activate()
        self.preferenceElements.append(submitButton)

        while True:
            p4 = self.win.getMouse()

            if self.quitButton.clicked(p4):
                exit(0)
            elif submitButton.clicked(p4):
                for i in self.preferenceElements:
                    i.undraw()
                for i in self.allViewElements:
                    i.undraw()
                newBusTraveler = BusinessTraveler(preferBusinessSelect, seatPreference)
                newBusTraveler.username = self.username
                newBusTraveler.password = self.password
                newBusTraveler.findBusTravelerSeats(self.plane)
                ticketView = TicketView(self.win, self.plane, newBusTraveler, self.manager)
                ticketView.outputPlaneDisplay()
                ticketView.outputInfo()
                ticketView.getButton()
                break
            elif self.touristButton.clicked(p4):
                self.checkTouristPreferences()
                break
            elif self.familyButton.clicked(p4):
                self.checkFamilyPreferences()
                break

    # ------------------------------------------------------------------

    def checkTouristPreferences(self):
        """
        Since Tourist preferences are already pre-set, only need to draw submit button and check if clicked
        """
        for i in self.preferenceElements:
            i.undraw()
        self.preferenceElements.clear()
        submitButton = Button(self.win, Point(25, 20), 12, 4, "Book Tickets")
        submitButton.rect.setFill(color_rgb(204, 107, 91))
        submitButton.activate()
        self.preferenceElements.append(submitButton)

        while True:
            p4 = self.win.getMouse()

            if self.quitButton.clicked(p4):
                quit(0)
            if submitButton.clicked(p4):
                for i in self.preferenceElements:
                    i.undraw()
                for i in self.allViewElements:
                    i.undraw()
                newTourist = Tourist(True)
                newTourist.findTouristSeats(self.plane)
                newTourist.username = self.username
                newTourist.password = self.password
                ticketView = TicketView(self.win, self.plane, newTourist, self.manager)
                ticketView.outputPlaneDisplay()
                ticketView.outputInfo()
                ticketView.getButton()
                break
            elif self.busTravelerButton.clicked(p4):
                self.checkBusPref1()
                break
            elif self.familyButton.clicked(p4):
                self.checkFamilyPreferences()
                break

    # ------------------------------------------------------------------

    def checkFamilyPreferences(self):
        """
        Draws row of buttons for family to select number of children
        Calls checkFamilyPreferences2 if one of the row 1 buttons have been clicked
        """
        for i in self.preferenceElements:
            i.undraw()
        self.preferenceElements.clear()

        preferenceText = Text(Point(24, 45), "Please select your preferences")
        preferenceText.setStyle("bold")
        preferenceText.setSize(16)
        preferenceText.setFace("courier")
        preferenceText.draw(self.win)
        self.preferenceElements.append(preferenceText)

        selectChildrenText = Text(Point(19, 42), "Select number of children")
        selectChildrenText.setFace("courier")
        selectChildrenText.draw(self.win)
        self.preferenceElements.append(selectChildrenText)

        oneChildButton = Button(self.win, Point(13, 38), 8, 4, "1 Child")
        oneChildButton.activate()
        self.preferenceElements.append(oneChildButton)

        twoChildrenButton = Button(self.win, Point(24, 38), 8, 4, "2 Children")
        twoChildrenButton.activate()
        self.preferenceElements.append(twoChildrenButton)

        threeChildrenButton = Button(self.win, Point(35, 38), 8, 4, "3 Children")
        threeChildrenButton.activate()
        self.preferenceElements.append(threeChildrenButton)

        while True:
            p2 = self.win.getMouse()

            if self.quitButton.clicked(p2):
                quit(0)
            elif oneChildButton.clicked(p2):
                numChildren = 1
                self.checkFamilyPreferences2(numChildren)
                break
            elif twoChildrenButton.clicked(p2):
                numChildren = 2
                self.checkFamilyPreferences2(numChildren)
                break
            elif threeChildrenButton.clicked(p2):
                numChildren = 3
                self.checkFamilyPreferences2(numChildren)
                break
            elif self.busTravelerButton.clicked(p2):
                self.checkBusPref1()
                break
            elif self.touristButton.clicked(p2):
                self.checkTouristPreferences()
                break

    # ------------------------------------------------------------------

    def checkFamilyPreferences2(self, numChildren: int):
        """
        Draws second row of buttons for family to choose seating preference
        Calls checkFamilyPreferences3 if row 2 button has been clicked
        :param numChildren: Result of which button has been clicked in row 1
        """
        seatPreferenceText = Text(Point(17, 32), "Seating Preference")
        seatPreferenceText.setFace("courier")
        seatPreferenceText.draw(self.win)
        self.preferenceElements.append(seatPreferenceText)

        windowPreferenceButton = Button(self.win, Point(13, 28), 8, 4, "Window")
        windowPreferenceButton.activate()
        self.preferenceElements.append(windowPreferenceButton)

        aislePreferenceButton = Button(self.win, Point(24, 28), 8, 4, "Aisle")
        aislePreferenceButton.activate()
        self.preferenceElements.append(aislePreferenceButton)

        noPreferenceButton = Button(self.win, Point(35, 28), 8, 4, "None")
        noPreferenceButton.activate()
        self.preferenceElements.append(noPreferenceButton)

        while True:
            p3 = self.win.getMouse()

            if self.quitButton.clicked(p3):
                exit(0)
            elif windowPreferenceButton.clicked(p3):
                seatPreference = "Window"
                self.checkFamilyPreferences3(numChildren, seatPreference)
                break
            elif aislePreferenceButton.clicked(p3):
                seatPreference = "Aisle"
                self.checkFamilyPreferences3(numChildren, seatPreference)
                break
            elif noPreferenceButton.clicked(p3):
                seatPreference = "None"
                self.checkFamilyPreferences3(numChildren, seatPreference)
                break
            elif self.busTravelerButton.clicked(p3):
                self.checkBusPref1()
                break
            elif self.touristButton.clicked(p3):
                self.checkTouristPreferences()
                break

    # ------------------------------------------------------------------

    def checkFamilyPreferences3(self, numChildren: int, seatPreference: str):
        """
        Draws submit button, calls ticket view if submit button clicked
        :param numChildren: Result of row 1 button click
        :param seatPreference: Result of row 2 button click
        """
        submitButton = Button(self.win, Point(25, 20), 12, 4, "Book Tickets")
        submitButton.rect.setFill(color_rgb(204, 107, 91))
        submitButton.activate()
        self.preferenceElements.append(submitButton)

        while True:
            p4 = self.win.getMouse()

            if self.quitButton.clicked(p4):
                exit(0)
            elif submitButton.clicked(p4):
                for i in self.preferenceElements:
                    i.undraw()
                for i in self.allViewElements:
                    i.undraw()
                newFamily = Family(numChildren, seatPreference)
                newFamily.username = self.username
                newFamily.password = self.password
                newFamily.findFamilySeats(self.plane)
                ticketView = TicketView(self.win, self.plane, newFamily, self.manager)
                ticketView.outputPlaneDisplay()
                ticketView.outputInfo()
                ticketView.getButton()
                break
            elif self.touristButton.clicked(p4):
                self.checkTouristPreferences()
                break

            elif self.busTravelerButton.clicked(p4):
                self.checkBusPref1()
                break

    # ------------------------------------------------------------------
