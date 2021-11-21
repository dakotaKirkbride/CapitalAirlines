
from graphics import *
from button import *
from Plane import *
from LoginView import *
from CategorySelectionView import *
from Manager import *
from ManagerView import *


class ManagerLoginView:

    # ------------------------------------------------------------------

    def __init__(self, win: GraphWin, plane: Plane):
        """
        Login view allows manager to log in with account credentials
        :param win: selected window object
        :param plane: selected plane object
        """
        self.win = win
        self.plane = plane
        self.allViewElements = []
        self.welcomeText = Text(Point(50, 65), "Welcome to Capital Airlines")
        self.managerText = Text(Point(50, 40), "Enter Manager Username and Password")
        self.managerUsername = Entry(Point(50, 36), 15)
        self.managerPassword = Entry(Point(50, 31), 15)
        self.submitButton = None
        self.returningUserText = Text(Point(50, 20), "Go Back?")
        self.returnToAccountButton = None
        self.quitButton = None

    # ------------------------------------------------------------------

    def formatElements(self):
        """
        format elements of manager login view
        """
        self.welcomeText.setSize(30)
        self.welcomeText.setFace("courier")
        self.welcomeText.draw(self.win)
        self.allViewElements.append(self.welcomeText)

        planeLogo = Image(Point(50, 52), "planeLogo.png")
        planeLogo.draw(self.win)
        self.allViewElements.append(planeLogo)

        self.managerText.setSize(16)
        self.managerText.setFace("courier")
        self.managerText.setStyle("bold")
        self.managerText.draw(self.win)
        self.allViewElements.append(self.managerText)

        self.managerUsername.setSize(16)
        self.managerUsername.draw(self.win)
        self.allViewElements.append(self.managerUsername)

        self.managerPassword.setSize(16)
        self.managerPassword.draw(self.win)
        self.allViewElements.append(self.managerPassword)

        self.submitButton = Button(self.win, Point(50, 26), 10, 3, "Submit")
        self.submitButton.activate()
        self.allViewElements.append(self.submitButton)

        self.returningUserText.setFace("courier")
        self.returningUserText.draw(self.win)
        self.allViewElements.append(self.returningUserText)

        self.returnToAccountButton = Button(self.win, Point(50, 16), 14, 3, "Return to Login")
        self.returnToAccountButton.activate()
        self.allViewElements.append(self.returnToAccountButton)

        self.quitButton = Button(self.win, Point(90, 10), 10, 5, "Quit")
        self.quitButton.activate()
        self.allViewElements.append(self.quitButton)

    # ------------------------------------------------------------------

    def getButton(self):
        """
        check for button click, call respective method
        """
        manager = Manager()

        status = True
        while status:
            p = self.win.getMouse()

            if self.quitButton.clicked(p):
                exit(0)

            if self.submitButton.clicked(p):
                username = self.managerUsername.getText()
                if username == manager.username:
                    password = self.managerPassword.getText()
                    if password == manager.password:
                        for i in self.allViewElements:
                            i.undraw()
                        managerView = ManagerView(self.win, self.plane)
                        managerView.outputPlaneDisplay()
                        managerView.displayManagerInfo()
                        managerView.getButton()
                        break
                    else:
                        self.managerText.setText("Invalid password, please try again")
                else:
                    self.managerText.setText("Invalid username, please try again")
            elif self.returnToAccountButton.clicked(p):
                for i in self.allViewElements:
                    i.undraw()
                break

    # ------------------------------------------------------------------
