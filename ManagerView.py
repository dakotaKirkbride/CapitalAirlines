
from graphics import *
from button import *
from Plane import *
from NewUserView import *
from Tourist import *
from BusinessTraveler import *
from Family import *
from Manager import *


class ManagerView:

    # ------------------------------------------------------------------

    def __init__(self, win: GraphWin, plane: Plane):
        """
        View seen when entered manager credentials
        :param win: selected window object
        :param plane: selected plane object
        """
        self.win = win
        self.plane = plane
        self.manager = Manager()
        self.allViewElements = []
        self.busTravelers = 0
        self.touristTravelers = 0
        self.familyTravelers = 0
        self.managerReportText = Text(Point(30, 65), "Capital Airlines Manager Report")
        self.flightText = Text(Point(15, 55), "CMH  ->  JFK")
        self.flightDescription = Text(Point(22, 50), "John Glenn International Airport to John F. Kennedy Airport")
        self.arriveDepartText = Text(Point(19, 45), "Depart 07:00              Arrive 09:30")
        self.locationText = Text(Point(22, 41), "Columbus, Ohio                       New York City, New York")
        self.seatsBookedText = Text(Point(10, 35), f"Seats Booked: {self.plane.seatsBooked}")
        self.seatsLeftText = Text(Point(12, 31), f"Seats Remaining: {self.plane.seatsLeft}")
        self.satisfactionIndex = Text(Point(15, 27), f"Average Satisfaction Level: {self.manager.generateReport(self.plane, False)}")
        self.breakdownText = Text(Point(11.5, 23), "Passenger Breakdown")
        self.busTravelersText = None
        self.touristGroupsText = None
        self.familyGroupsText = None
        self.cmdReport = None
        self.signOutButton = None

    # ------------------------------------------------------------------

    def outputPlaneDisplay(self):
        """
        output up-to-date plane view
        """
        seatIndex = 0
        seatXaxis = 77
        seatXaxis2 = 79
        seatYaxis = 69
        seatYaxis2 = 67

        frontText = Text(Point(87, 72), "Front of Plane").draw(self.win)
        self.allViewElements.append(frontText)

        for row in range(self.plane.rows):
            for seat in range(self.plane.seatsPerRow):
                if self.plane.planeMatrix[seatIndex] == 0:
                    newSeat = Rectangle(Point(seatXaxis, seatYaxis), Point(seatXaxis2, seatYaxis2))
                    newSeat.setFill("white")
                    newSeat.draw(self.win)

                elif self.plane.planeMatrix[seatIndex] == 1:
                    newSeat = Rectangle(Point(seatXaxis, seatYaxis), Point(seatXaxis2, seatYaxis2))
                    newSeat.setFill(color_rgb(195, 99, 64))
                    newSeat.draw(self.win)
                    self.busTravelers += 1
                elif self.plane.planeMatrix[seatIndex] == 2:
                    newSeat = Rectangle(Point(seatXaxis, seatYaxis), Point(seatXaxis2, seatYaxis2))
                    newSeat.setFill(color_rgb(66, 147, 88))
                    newSeat.draw(self.win)
                    self.touristTravelers += 1
                else:
                    newSeat = Rectangle(Point(seatXaxis, seatYaxis), Point(seatXaxis2, seatYaxis2))
                    newSeat.setFill(color_rgb(15, 83, 141))
                    newSeat.draw(self.win)
                    self.familyTravelers += 1

                if row < 2:
                    newSeat.setOutline(color_rgb(206, 97, 78))

                if seat == 2:
                    seatXaxis += 5
                    seatXaxis2 += 5
                else:
                    seatXaxis += 3
                    seatXaxis2 += 3
                seatIndex += 1

                self.allViewElements.append(newSeat)

            seatXaxis = 77
            seatXaxis2 = 79
            seatYaxis -= 3
            seatYaxis2 -= 3

        backText = Text(Point(86.5, 6), "Back of Plane").draw(self.win)
        self.allViewElements.append(backText)

    # ------------------------------------------------------------------

    def displayManagerInfo(self):
        """
        display contents of manager view
        """
        self.managerReportText.setSize(30)
        self.managerReportText.setFace("courier")
        self.managerReportText.draw(self.win)
        self.allViewElements.append(self.managerReportText)

        self.flightText.setSize(34)
        self.flightText.setStyle("bold")
        self.flightText.draw(self.win)
        self.allViewElements.append(self.flightText)

        self.flightDescription.setSize(16)
        self.flightDescription.draw(self.win)
        self.allViewElements.append(self.flightDescription)

        self.arriveDepartText.setSize(22)
        self.arriveDepartText.draw(self.win)
        self.allViewElements.append(self.arriveDepartText)

        self.locationText.setSize(16)
        self.locationText.draw(self.win)
        self.allViewElements.append(self.locationText)

        self.signOutButton = Button(self.win, Point(50, 7), 12, 4, "Sign out")
        self.signOutButton.activate()
        self.allViewElements.append(self.signOutButton)

        self.cmdReport = Button(self.win, Point(30, 7), 12, 4, "Print report in cmd")
        self.cmdReport.activate()
        self.allViewElements.append(self.cmdReport)

        self.seatsBookedText.draw(self.win)
        self.seatsBookedText.setSize(17)
        self.allViewElements.append(self.seatsBookedText)

        self.seatsLeftText.draw(self.win)
        self.seatsLeftText.setSize(17)
        self.allViewElements.append(self.seatsLeftText)

        self.satisfactionIndex.draw(self.win)
        self.satisfactionIndex.setSize(17)
        self.allViewElements.append(self.satisfactionIndex)

        self.breakdownText.draw(self.win)
        self.breakdownText.setSize(17)
        self.allViewElements.append(self.breakdownText)

        self.busTravelersText = Text(Point(12.5, 20), f"Business Passengers: {self.busTravelers}")
        self.busTravelersText.draw(self.win)
        self.allViewElements.append(self.busTravelersText)

        self.touristGroupsText = Text(Point(11.5, 17), f"Tourist Passengers: {self.touristTravelers}")
        self.touristGroupsText.draw(self.win)
        self.allViewElements.append(self.touristGroupsText)

        self.familyGroupsText = Text(Point(11.5, 14), f"Family Passengers: {self.familyTravelers}")
        self.familyGroupsText.draw(self.win)
        self.allViewElements.append(self.familyGroupsText)

        legendText = Text(Point(60, 60), "Legend")
        legendText.setStyle("bold")
        legendText.draw(self.win)
        self.allViewElements.append(legendText)

        openBox = Rectangle(Point(57, 57), Point(59, 55))
        openBox.setFill("white")
        openBox.draw(self.win)
        self.allViewElements.append(openBox)
        openSeatText = Text(Point(64, 56), "- Open Seat").draw(self.win)
        self.allViewElements.append(openSeatText)

        openBox2 = Rectangle(Point(57, 53), Point(59, 51))
        openBox2.setOutline(color_rgb(206, 97, 78))
        openBox2.draw(self.win)
        self.allViewElements.append(openBox2)
        busSelectBox = Text(Point(66.5, 52), "- Business Select Seat").draw(self.win)
        self.allViewElements.append(busSelectBox)

        openBox3 = Rectangle(Point(57, 49), Point(59, 47))
        openBox3.setFill(color_rgb(195, 99, 64))
        openBox3.draw(self.win)
        self.allViewElements.append(openBox3)
        busTravelerBox = Text(Point(66.5, 48), "- Business Traveler Seat").draw(self.win)
        self.allViewElements.append(busTravelerBox)

        openBox4 = Rectangle(Point(57, 45), Point(59, 43))
        openBox4.setFill(color_rgb(66, 147, 88))
        openBox4.draw(self.win)
        self.allViewElements.append(openBox4)
        touristBox = Text(Point(64, 44), "- Tourist Seat").draw(self.win)
        self.allViewElements.append(touristBox)

        openBox5 = Rectangle(Point(57, 41), Point(59, 39))
        openBox5.setFill(color_rgb(15, 83, 141))
        openBox5.draw(self.win)
        self.allViewElements.append(openBox5)
        familyBox = Text(Point(64, 40), "- Family Seat").draw(self.win)
        self.allViewElements.append(familyBox)

    # ------------------------------------------------------------------

    def getButton(self):
        """
        check for button click, call respective method
        """
        while True:
            p = self.win.getMouse()

            if self.signOutButton.clicked(p):
                for i in self.allViewElements:
                    i.undraw()
                break

            if self.cmdReport.clicked(p):
                self.plane.printMatrix()
                self.manager.generateReport(self.plane, True)

    # ------------------------------------------------------------------
