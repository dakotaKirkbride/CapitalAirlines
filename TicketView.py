
from graphics import *
from button import *
from Plane import *
from Manager import *
from NewUserView import *
from Tourist import *
from BusinessTraveler import *
from Family import *
from random import randrange


class TicketView:

    # ------------------------------------------------------------------

    def __init__(self, win: GraphWin, plane: Plane, passengerGroup, manager: Manager):
        """
        View that displays the booked tickets for the user based on their selections in the previous view
        :param win: Selected window object
        :param plane: Selected plane object
        :param passengerGroup: The passenger object for which tickets are being shown
        :param manager: Selected manager object
        """
        self.win = win
        self.plane = plane
        self.manager = manager
        self.passengerGroup = passengerGroup
        self.allViewElements = []
        self.planeElements = []
        self.congratsText = Text(Point(22, 65), f"Ticket Report for {self.passengerGroup.username}")
        self.ticketID = Text(Point(14, 58), f"Ticket ID: {randrange(1000000000)}")
        self.flightText = Text(Point(15, 52), "CMH  ->  JFK")
        self.flightDescription = Text(Point(22, 47), "John Glenn International Airport to John F. Kennedy Airport")
        self.arriveDepartText = Text(Point(19, 42), "Depart 07:00              Arrive 09:30")
        self.locationText = Text(Point(22, 38), "Columbus, Ohio                       New York City, New York")
        self.passengersText = Text(Point(15, 28), f"Number of Passengers: {self.passengerGroup.numPassengers}")
        self.changeSeatButton = None
        self.signOutButton = None

    # ------------------------------------------------------------------

    def outputPlaneDisplay(self):
        """
        Displays an up-to-date plane view
        """
        seatIndex = 0
        seatXaxis = 77
        seatXaxis2 = 79
        seatYaxis = 69
        seatYaxis2 = 67

        frontText = Text(Point(87, 72), "Front of Plane").draw(self.win)
        self.allViewElements.append(frontText)

        # iterate over each row in the plane
        for row in range(self.plane.rows):
            # iterate over each seat in given row
            for seat in range(self.plane.seatsPerRow):
                # if one of the booked ticket seat numbers are the same as the current seat number
                if seatIndex in self.passengerGroup.bookedTickets.values():
                    # draw a slightly larger version of the rectangle, in blue
                    newSeat = Rectangle(Point(seatXaxis - 0.2, seatYaxis + 0.2), Point(seatXaxis2 + 0.2, seatYaxis2 - 0.2))
                    newSeat.setFill(color_rgb(13, 62, 140))
                    newSeat.draw(self.win)
                # elif the current seat is occupied by another group
                elif self.plane.planeMatrix[seatIndex] >= 1:
                    # draw grey rectangle
                    newSeat = Rectangle(Point(seatXaxis, seatYaxis), Point(seatXaxis2, seatYaxis2))
                    newSeat.setFill("grey")
                    newSeat.draw(self.win)
                else:
                    # empty seats are white
                    newSeat = Rectangle(Point(seatXaxis, seatYaxis), Point(seatXaxis2, seatYaxis2))
                    newSeat.setFill("white")
                    newSeat.draw(self.win)

                if row < 2:
                    # outline bus select seats with red
                    newSeat.setOutline(color_rgb(206, 97, 78))
                # if the left aisle seat, increase distance from next seat to give illusion of an aisle
                if seat == 2:
                    seatXaxis += 5
                    seatXaxis2 += 5
                else:
                    seatXaxis += 3
                    seatXaxis2 += 3
                seatIndex += 1

                self.allViewElements.append(newSeat)
                self.planeElements.append(newSeat)

            seatXaxis = 77
            seatXaxis2 = 79
            seatYaxis -= 3
            seatYaxis2 -= 3

        backText = Text(Point(86.5, 6), "Back of Plane").draw(self.win)
        self.allViewElements.append(backText)

    # ------------------------------------------------------------------

    def outputInfo(self):
        """
        Displays ticket information
        """
        self.congratsText.setSize(30)
        self.congratsText.setFace("courier")
        self.congratsText.draw(self.win)
        self.allViewElements.append(self.congratsText)

        self.ticketID.setFace("courier")
        self.ticketID.setSize(18)
        self.ticketID.draw(self.win)
        self.allViewElements.append(self.ticketID)

        # self.flightText.setFace("courier")
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

        self.passengersText.setSize(18)
        self.passengersText.setStyle("bold")
        self.passengersText.draw(self.win)
        self.allViewElements.append(self.passengersText)

        passengerPointY = 25
        for i in range(len(self.passengerGroup.bookedTickets)):
            newText = Text(Point(12, passengerPointY), f"Booked Seat: {self.passengerGroup.bookedTickets[i]}")
            newText.setSize(15)
            newText.draw(self.win)
            self.allViewElements.append(newText)
            passengerPointY -= 2

        self.changeSeatButton = Button(self.win, Point(20, 10), 12, 4, "Change Seats")
        self.changeSeatButton.activate()
        self.allViewElements.append(self.changeSeatButton)

        self.signOutButton = Button(self.win, Point(50, 10), 12, 4, "Sign out")
        self.signOutButton.activate()
        self.allViewElements.append(self.signOutButton)

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
        openBox2.setFill("grey")
        openBox2.draw(self.win)
        self.allViewElements.append(openBox2)
        takenSeatText = Text(Point(64, 52), "- Taken Seat").draw(self.win)
        self.allViewElements.append(takenSeatText)
        openBox3 = Rectangle(Point(57, 49), Point(59, 47))
        openBox3.setOutline(color_rgb(206, 97, 78))
        openBox3.draw(self.win)
        self.allViewElements.append(openBox3)
        busSelectText = Text(Point(66.5, 48), "- Business Select Seat").draw(self.win)
        self.allViewElements.append(busSelectText)
        openBox4 = Rectangle(Point(56.8, 45.2), Point(59.2, 42.8))
        openBox4.setFill(color_rgb(13, 62, 140))
        openBox4.draw(self.win)
        self.allViewElements.append(openBox4)
        bookedSeatText = Text(Point(65.5, 44), "- Your Booked Seat").draw(self.win)
        self.allViewElements.append(bookedSeatText)

    # ------------------------------------------------------------------

    def getButton(self):
        """
        Checks for button click, calls respective method based on button clicked
        """
        while True:
            p = self.win.getMouse()

            if self.changeSeatButton.clicked(p):

                if self.passengerGroup.changeSeatChances > 0:
                    for i in self.allViewElements:
                        i.undraw()
                    self.passengerGroup.changeSeats(self.plane)
                    self.outputPlaneDisplay()
                    self.outputInfo()
                else:
                    self.changeSeatButton.deactivate()

            elif self.signOutButton.clicked(p):
                self.manager.writeToCSV(self.plane)
                for i in self.allViewElements:
                    i.undraw()
                break
