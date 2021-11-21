

from Plane import *
from BusinessTraveler import *
from Tourist import *
from Family import *
from random import choice
from random import randrange
import csv


class Manager:

    # ------------------------------------------------------------------

    def __init__(self):
        """
        Manager has ability to see manager screen in GUI based off of below login credentials
        """
        self.username = "manager"
        self.password = "test"

    # ------------------------------------------------------------------

    def generateReport(self, plane: Plane, printToCmd: bool):
        """
        Creates a report of passengers on flight. Randomly selects the satisfaction value of 10 random users
        on board and returns the average score
        :param plane: selected plane object
        :param printToCmd: prints report to terminal if true, returns report to GUI if false
        :return: average satisfaction score
        """
        randomSatisfactionTotal = 0

        if printToCmd:
            if plane.passengerGroupNums < 10:
                print("Not enough passengers booked to generate report. Please try again later")
            else:
                for i in range(10):
                    randomSatisfactionLevel = choice(list(plane.passengerGroups.values()))
                    randomSatisfactionTotal += randomSatisfactionLevel
                print("Average Satisfaction Level of 10 passenger groups:", randomSatisfactionTotal / 10)
        else:
            if plane.passengerGroupNums < 10:
                return "N/A"
            else:
                for i in range(10):
                    randomSatisfactionLevel = choice(list(plane.passengerGroups.values()))
                    randomSatisfactionTotal += randomSatisfactionLevel
                return randomSatisfactionTotal / 10

    # ------------------------------------------------------------------

    def generateRandomPassengers(self, plane: Plane, minNum: int, maxNum: int):
        """
        Creates a random number of passenger groups, with different preferences, and calls
        necessary methods to add passengers to plane
        :param plane: selected plane object
        :param minNum: minimum number of passenger groups to be added
        :param maxNum: maximum number of passenger groups to be added
        """
        passengersList = []

        for i in range(randrange(minNum, maxNum)):
            pickPassengerType = randrange(1, 4)
            if pickPassengerType == 1:
                pickBusSelect = randrange(1, 3)
                if pickBusSelect == 1:
                    preferBusSelect = True
                else:
                    preferBusSelect = False
                pickSeatingPreference = randrange(1, 4)
                if pickSeatingPreference == 1:
                    seatingPreference = "Window"
                elif pickSeatingPreference == 2:
                    seatingPreference = "Aisle"
                else:
                    seatingPreference = "None"
                newBusTraveler = BusinessTraveler(preferBusSelect, seatingPreference)
                newBusTraveler.username = f"BusPassenger{randrange(1000)}"
                newBusTraveler.password = f"{randrange(10000)}"
                passengersList.append(newBusTraveler)
            elif pickPassengerType == 2:
                newTourist = Tourist()
                newTourist.username = f"Tourist{randrange(1000)}"
                newTourist.password = f"{randrange(10000)}"
                passengersList.append(newTourist)
            else:
                pickNumChildren = randrange(1, 4)
                pickSeatingPreference = randrange(1, 4)
                if pickSeatingPreference == 1:
                    seatingPreference = "Window"
                elif pickSeatingPreference == 2:
                    seatingPreference = "Aisle"
                else:
                    seatingPreference = "None"
                newFamily = Family(pickNumChildren, seatingPreference)
                newFamily.username = f"Family{randrange(1000)}"
                newFamily.password = f"{randrange(10000)}"
                passengersList.append(newFamily)

        # add random passengers to csv file
        filename = "passengers.csv"
        with open(filename, 'w', newline='') as csvFile:
            fieldnames = ["passengerType", "username", "password", "preferBusSelect", "seatPref", "numChildren"]
            writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
            writer.writeheader()
            for passenger in passengersList:
                writer.writerow(passenger.dictionary())

    # ------------------------------------------------------------------

    def writeToCSV(self, plane: Plane, filename: str = "passengers.csv"):
        """
        Write current passengers to csv file
        :param plane: selected plane object
        :param filename: csv filename
        """
        with open(filename, 'w', newline='') as csvFile:
            fieldnames = ["passengerType", "username", "password", "preferBusSelect", "seatPref", "numChildren"]
            writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
            writer.writeheader()
            for passenger in plane.passengerGroups.keys():
                writer.writerow(passenger.dictionary())

    # ------------------------------------------------------------------------------------------------------------------------------------

    def clearCSV(self, plane: Plane, filename: str = "passengers.csv"):
        """
        Clears csv file of all passengers
        :param plane: selected plane object
        :param filename: csv filename
        """
        with open(filename, 'w', newline='') as csvFile:
            fieldnames = ["passengerType", "username", "password", "preferBusSelect", "seatPref", "numChildren"]
            writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
            writer.writeheader()

    # ------------------------------------------------------------------------------------------------------------------------------------

    def readFromCSV(self, plane: Plane, filename: str = "passengers.csv"):
        """
        Read CSV file, add passengers to plane object
        :param plane: selected plane object
        :param filename: csv filename
        """
        with open(filename, newline='') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                if list(row.values())[0] == "t":
                    newPassenger = Tourist()
                    newPassenger.username = list(row.values())[1]
                    newPassenger.password = list(row.values())[2]
                    newPassenger.findTouristSeats(plane)
                    plane.passengerAccounts[newPassenger.username] = newPassenger.password
                elif list(row.values())[0] == "b":
                    if list(row.values())[3] == "True":
                        busSelectPref = True
                    else:
                        busSelectPref = False
                    seatPref = list(row.values())[4]
                    newPassenger = BusinessTraveler(busSelectPref, seatPref)
                    newPassenger.username = list(row.values())[1]
                    newPassenger.password = list(row.values())[2]
                    newPassenger.findBusTravelerSeats(plane)
                    plane.passengerAccounts[newPassenger.username] = newPassenger.password
                elif list(row.values())[0] == "f":
                    seatPref = list(row.values())[4]
                    numChildren = int(list(row.values())[5])
                    newPassenger = Family(numChildren, seatPref)
                    newPassenger.username = list(row.values())[1]
                    newPassenger.password = list(row.values())[2]
                    newPassenger.findFamilySeats(plane)
                    plane.passengerAccounts[newPassenger.username] = newPassenger.password

    # ------------------------------------------------------------------------------------------------------------------------------------
