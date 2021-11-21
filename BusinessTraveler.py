

from Plane import *
from random import randrange


class BusinessTraveler:

    # ------------------------------------------------------------------

    def __init__(self, preferBusSelect: bool, seatPreference: str):
        """
        Business Travelers will always sit alone. They can request either business select or
        regular seats. Can also indicate a seating preference
        :param preferBusSelect: True indicates business select preference, False indicates regular seating
        :param seatPreference: Seating preference can be "Window", "Aisle", or "None"
        """
        self.numPassengers = 1
        self.username = ""
        self.password = ""
        self.satisfactionLevel = 0
        # holds number in passenger group as key, seat index as value
        self.bookedTickets = {}
        self.preferBusSelect = preferBusSelect
        # Must be either "Window", "Aisle", or "None"
        self.seatPreference = seatPreference
        self.changeSeatChances = 3

    # ------------------------------------------------------------------

    def findBusTravelerSeats(self, plane: Plane, startIndex=12):
        """
        function that algorithmically finds the best possible seating arrangement for the given business traveler
        :param plane: plane object to search through
        :param startIndex: starting index of where algorithm should begin looking for seats. It's an optional value,
        and will only be used in instances where the traveler chooses to change seats
        :return: calls bookBusTravelerTickets method, which books the tickets
        """
        # hold garbage values for now
        bestSatisfactionLevel = -100
        bestSeatIndex = -1

        # this is the default option for a bus traveler first being assigned seats who prefers bus select
        if self.preferBusSelect and startIndex >= 12:
            rowRange = range(0, plane.rows)
            seatIndex = 0
            startIndex = 0
        # this option will be called when the bus traveler chooses to change seats but still prefers bus select
        elif self.preferBusSelect and startIndex < 12:
            rowRange = range(0, plane.rows)
            seatIndex = 0
        # bus traveler prefers regular seating
        else:
            rowRange = range(2, plane.rows)
            seatIndex = 12

        for row in rowRange:
            for seat in range(plane.seatsPerRow):
                if seatIndex >= startIndex:
                    tempSatisfactionLevel = -100
                    # iterating over a window seat
                    if seat == 0 or seat == (plane.seatsPerRow - 1):
                        if plane.planeMatrix[seatIndex] == 0:
                            if self.seatPreference == "Window" or self.seatPreference == "None":
                                tempSatisfactionLevel = 5
                            elif self.seatPreference == "Aisle":
                                tempSatisfactionLevel = 0
                            if row >= 2 and self.preferBusSelect:
                                tempSatisfactionLevel -= 5
                    # iterating over an aisle seat
                    elif seat == 2 or seat == 3:
                        if plane.planeMatrix[seatIndex] == 0:
                            if self.seatPreference == "Aisle" or self.seatPreference == "None":
                                tempSatisfactionLevel = 5
                            elif self.seatPreference == "Window":
                                tempSatisfactionLevel = 0
                            if row >= 2 and self.preferBusSelect:
                                tempSatisfactionLevel -= 5
                    # iterating over a middle seat
                    elif seat == 1 or seat == 4:
                        if plane.planeMatrix[seatIndex] == 0:
                            if self.seatPreference == "None":
                                tempSatisfactionLevel = 5
                            elif self.seatPreference == "Window" or self.seatPreference == "Aisle":
                                tempSatisfactionLevel = 0
                            if row >= 2 and self.preferBusSelect:
                                tempSatisfactionLevel -= 5

                    if tempSatisfactionLevel > bestSatisfactionLevel:
                        bestSatisfactionLevel = tempSatisfactionLevel
                        bestSeatIndex = seatIndex
                seatIndex += 1

        self.satisfactionLevel = bestSatisfactionLevel
        self.bookBusTravelerTickets(bestSeatIndex, plane)

    # ------------------------------------------------------------------

    def changeSeats(self, plane: Plane):
        """
        Calls above method with modified start index for bus traveler to change seating
        :param plane: plane object to search through
        :return: calls above method
        """
        # get the seat that comes right after the passengers already-booked seat
        nextAvailableSeat = (list(self.bookedTickets.values())[-1]) + 1
        numBookedSeats = len(self.bookedTickets)

        # user has 3 chances to change seating
        if self.changeSeatChances == 0:
            print("Out of chances to change seating")
        else:
            self.changeSeatChances -= 1
            for i in range(numBookedSeats):
                bookedSeatIndex = self.bookedTickets[i]
                # unassign previously booked ticket
                plane.planeMatrix[bookedSeatIndex] = 0
                plane.seatsBooked -= 1
            # delete instance of this user from planes passenger group dictionary
            del plane.passengerGroups[self]
            # call above method with next available seat
            self.findBusTravelerSeats(plane, nextAvailableSeat)

    # ------------------------------------------------------------------

    def bookBusTravelerTickets(self, bestSeatIndex: int, plane: Plane):
        """
        Book seats based on info gathered from findSeats method
        :param bestSeatIndex: index of best possible seat for user
        :param plane: plane object to search through
        :return: updates user's booked tickets {}, planes passenger groups {}, and plane matrix []
        """
        self.bookedTickets[0] = bestSeatIndex
        plane.planeMatrix[bestSeatIndex] = 1
        plane.seatsBooked += 1
        plane.seatsLeft = plane.totalSeats - plane.seatsBooked
        plane.passengerGroups[self] = self.satisfactionLevel
        plane.passengerGroupNums += 1

    # ------------------------------------------------------------------

    def dictionary(self):
        """
        :return: Dictionary formatted for CSV file input
        """
        return {"passengerType": "b", "username": self.username, "password": self.password, "preferBusSelect": self.preferBusSelect, "seatPref": self.seatPreference}

    # ------------------------------------------------------------------
