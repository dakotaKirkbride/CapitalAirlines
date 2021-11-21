

from Plane import *
from random import randrange


class Family:

    # ------------------------------------------------------------------

    def __init__(self, numChildren: int, seatPreference: str):
        """
        Families will consist of 2 parents and 1-3 children, and will prefer to be seated together if possible
        :param numChildren: number of children
        :param seatPreference: seating preference
        """
        self.numAdults = 2
        self.numChildren = numChildren
        self.numPassengers = self.numAdults + self.numChildren
        self.username = ""
        self.password = ""
        self.satisfactionLevel = 0
        # holds number in passenger group as key, seat index as value
        self.bookedTickets = {}
        # Must be either "Window", "Aisle", or "None"
        self.seatPreference = seatPreference
        self.changeSeatChances = 3

    # ------------------------------------------------------------------

    def findFamilySeats(self, plane: Plane, startIndex=12):
        """
        function that algorithmically finds the best possible seating arrangement for the given tourists
        :param plane: plane object to search through
        :param startIndex: starting index of where algorithm should begin looking for seats. It's an optional value,
        and will only be used in instances where the tourist chooses to change seats
        :return: calls bookBusTouristTickets method, which books the tickets
        :return:
        """
        # holds best possible satisfaction level based on ideal seating arrangement
        # junk value for now
        bestSatisfactionLevel = -100
        # index of best possible seating arrangement
        # junk value for now
        bestSeatIndex = -1
        # signals if all family member can sit together
        canSitTogetherOnPlane = False
        seatIndex = 12

        for row in range(2, plane.rows):
            for seat in range(plane.seatsPerRow):
                if seatIndex >= startIndex:
                    tempSatisfactionLevel = -100
                    canSitTogetherInSeat = True
                    # if family could sit together in the same row
                    if seat in range(0, plane.seatsPerRow - self.numPassengers):
                        passengerNum = 0
                        for possibleSeat in range(seatIndex, seatIndex + self.numPassengers):
                            if possibleSeat > 119:
                                break
                            # if the seat being considered is already booked
                            if plane.planeMatrix[possibleSeat] != 0 and passengerNum == 0:
                                canSitTogetherInSeat = False
                                break
                            elif plane.planeMatrix[possibleSeat] != 0 and passengerNum > 0:
                                # Subtract 10 from satisfaction level if passengers can't sit together
                                tempSatisfactionLevel = -10
                                # canSitTogetherInSeat is set to false
                                canSitTogetherInSeat = False
                            passengerNum += 1
                        # if the passengers can sit together, add 10 to temp value
                        if canSitTogetherInSeat:
                            tempSatisfactionLevel = 10
                            canSitTogetherOnPlane = True
                    elif seat not in range(0, plane.seatsPerRow - self.numPassengers):
                        if plane.planeMatrix[seatIndex] == 0:
                            canSitTogetherInSeat = False
                            tempSatisfactionLevel = -10

                    if tempSatisfactionLevel > bestSatisfactionLevel and plane.planeMatrix[seatIndex] == 0:
                        bestSatisfactionLevel = tempSatisfactionLevel
                        bestSeatIndex = seatIndex
                seatIndex += 1

        self.satisfactionLevel = bestSatisfactionLevel
        self.bookFamilyTickets(canSitTogetherOnPlane, bestSeatIndex, plane)

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
            self.findFamilySeats(plane, nextAvailableSeat)

    # ------------------------------------------------------------------

    def bookFamilyTickets(self, canSitTogetherOnPlane: bool, bestSeatIndex: int, plane: Plane):
        """
        Book seats based on info gathered from findSeats method
        :param canSitTogetherOnPlane: true if users can be seating next to each other
        :param bestSeatIndex: index of best possible seat for user
        :param plane: plane object to search through
        :return: updates user's booked tickets {}, planes passenger groups {}, and plane matrix []
        """
        familyIndex = 0
        # if can sit together, assign user to best seat index and seats after
        if canSitTogetherOnPlane:
            for i in range(bestSeatIndex, bestSeatIndex + self.numPassengers):
                self.bookedTickets[familyIndex] = i
                plane.planeMatrix[i] = 3
                plane.seatsBooked += 1
                familyIndex += 1
        else:
            # if can't sit together, must seat second user in next available seat
            while len(self.bookedTickets) < self.numPassengers:
                if plane.planeMatrix[bestSeatIndex] == 0:
                    self.bookedTickets[familyIndex] = bestSeatIndex
                    plane.planeMatrix[bestSeatIndex] = 3
                    plane.seatsBooked += 1
                bestSeatIndex += 1
                familyIndex += 1
        plane.seatsLeft = plane.totalSeats - plane.seatsBooked
        plane.passengerGroups[self] = self.satisfactionLevel
        plane.passengerGroupNums += 1

    # ------------------------------------------------------------------

    def dictionary(self):
        """
        :return: Dictionary formatted for CSV file input
        """
        return {"passengerType": "f", "username": self.username, "password": self.password, "seatPref": self.seatPreference, "numChildren": self.numChildren}

    # ------------------------------------------------------------------
