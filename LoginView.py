

from graphics import *
from button import *
from Plane import *
from Manager import *
from NewUserView import *
from CategorySelectionView import *
from ManagerView import *
from ManagerLoginView import *


class LoginView:

    # ------------------------------------------------------------------

    def __init__(self, win: GraphWin, manager: Manager):
        """
        Login view allows user to log in with account credentials, or access other views
        :param win: selected window
        """
        self.win = win
        self.manager = manager
        self.allViewElements = []
        self.welcomeText = Text(Point(50, 65), "Welcome to Capital Airlines")
        self.loginText = Text(Point(50, 40), "Login Here")
        self.loginUsername = Entry(Point(50, 36), 15)
        self.loginPassword = Entry(Point(50, 31), 15)
        self.submitLoginButton = None
        self.newUserText = Text(Point(50, 20), "New User?")
        self.createAccountButton = None
        self.managerButton = None
        self.quitButton = None

    # ------------------------------------------------------------------

    def formatElements(self):
        """
        format LoginView elements in window
        :return:
        """
        self.welcomeText.setSize(30)
        self.welcomeText.setFace("courier")
        self.welcomeText.draw(self.win)
        self.allViewElements.append(self.welcomeText)

        # Will need hardcoded in to work
        planeLogo = Image(Point(50, 52), "planeLogo.png")
        planeLogo.draw(self.win)
        self.allViewElements.append(planeLogo)

        self.loginText.setSize(16)
        self.loginText.setFace("courier")
        self.loginText.setStyle("bold")
        self.loginText.draw(self.win)
        self.allViewElements.append(self.loginText)

        self.loginUsername.setSize(16)
        self.loginUsername.draw(self.win)
        self.allViewElements.append(self.loginUsername)

        self.loginPassword.setSize(16)
        self.loginPassword.draw(self.win)
        self.allViewElements.append(self.loginPassword)

        self.submitLoginButton = Button(self.win, Point(50, 26), 10, 3, "Submit")
        self.submitLoginButton.activate()
        self.allViewElements.append(self.submitLoginButton)

        self.newUserText.setFace("courier")
        self.newUserText.draw(self.win)
        self.allViewElements.append(self.newUserText)

        self.createAccountButton = Button(self.win, Point(50, 16), 14, 3, "Create an Account")
        self.createAccountButton.activate()
        self.allViewElements.append(self.createAccountButton)

        self.managerButton = Button(self.win, Point(10, 10), 10, 5, "Manager")
        self.managerButton.activate()
        self.allViewElements.append(self.managerButton)

        self.quitButton = Button(self.win, Point(90, 10), 10, 5, "Quit")
        self.quitButton.activate()
        self.allViewElements.append(self.quitButton)

    # ------------------------------------------------------------------

    def getButton(self, plane: Plane):
        """
        Checks for button click, calls next view object based on button clicked
        """
        while True:
            p = self.win.getMouse()

            if self.quitButton.clicked(p):
                exit(0)
            # if submit button clicked, get username and password entered
            elif self.submitLoginButton.clicked(p):
                userName = self.loginUsername.getText()
                password = self.loginPassword.getText()
                # if username is on file
                if userName in plane.passengerAccounts.keys():
                    # if the password matches the password for the given username
                    if password == plane.passengerAccounts[userName]:
                        for passengerGroup in plane.passengerGroups.keys():
                            if passengerGroup.username == userName and passengerGroup.password == password:
                                # undraw all elements in view
                                for i in self.allViewElements:
                                    i.undraw()
                                # call ticket view
                                ticketView = TicketView(self.win, plane, passengerGroup, self.manager)
                                ticketView.outputPlaneDisplay()
                                ticketView.outputInfo()
                                ticketView.getButton()
                                break
                        self.formatElements()
                        self.loginUsername.setText("")
                        self.loginPassword.setText("")
                    else:
                        self.loginText.setText("Incorrect password, please try again")
                else:
                    self.loginText.setText("Username not found, please try again")
            elif self.createAccountButton.clicked(p):
                for i in self.allViewElements:
                    i.undraw()
                createAccountView = NewUserView(self.win, self.manager)
                createAccountView.formatElements()
                createAccountView.getButton(plane)
                self.formatElements()
            elif self.managerButton.clicked(p):
                for i in self.allViewElements:
                    i.undraw()
                managerLoginView = ManagerLoginView(self.win, plane)
                managerLoginView.formatElements()
                managerLoginView.getButton()
                self.formatElements()

    # ------------------------------------------------------------------

