
from graphics import *
from button import *
from Plane import *
from Manager import *
from LoginView import *
from CategorySelectionView import *


class NewUserView:

    # ------------------------------------------------------------------

    def __init__(self, win: GraphWin, manager: Manager):
        """
        View for new users to add username and password information
        :param win: selected window object
        :param manager: selected manager object
        """
        self.win = win
        self.manager = manager
        self.allViewElements = []
        self.welcomeText = Text(Point(50, 65), "Welcome to Capital Airlines")
        self.newUserText = Text(Point(50, 40), "Enter new username and password")
        self.newUserUsername = Entry(Point(50, 36), 15)
        self.newUserPassword = Entry(Point(50, 31), 15)
        self.submitNewUserButton = None
        self.returningUserText = Text(Point(50, 20), "Returning User?")
        self.returnToAccountButton = None
        self.quitButton = None

    # ------------------------------------------------------------------

    def formatElements(self):
        """
        formats the elements of the view
        """
        self.welcomeText.setSize(30)
        self.welcomeText.setFace("courier")
        self.welcomeText.draw(self.win)
        self.allViewElements.append(self.welcomeText)

        planeLogo = Image(Point(50, 52), "planeLogo.png")
        planeLogo.draw(self.win)
        self.allViewElements.append(planeLogo)

        self.newUserText.setSize(16)
        self.newUserText.setFace("courier")
        self.newUserText.setStyle("bold")
        self.newUserText.draw(self.win)
        self.allViewElements.append(self.newUserText)

        self.newUserUsername.setSize(16)
        self.newUserUsername.draw(self.win)
        self.allViewElements.append(self.newUserUsername)

        self.newUserPassword.setSize(16)
        self.newUserPassword.draw(self.win)
        self.allViewElements.append(self.newUserPassword)

        self.submitNewUserButton = Button(self.win, Point(50, 26), 10, 3, "Submit")
        self.submitNewUserButton.activate()
        self.allViewElements.append(self.submitNewUserButton)

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

    def getButton(self, plane: Plane):
        """
        Checks for button click, calls next view object based on button clicked
        :param plane: selected plane object
        """
        status = True
        while status:
            p = self.win.getMouse()

            if self.quitButton.clicked(p):
                exit(0)

            if self.submitNewUserButton.clicked(p):
                newUsername = self.newUserUsername.getText()
                newPassword = self.newUserPassword.getText()
                if newUsername != "":
                    if newPassword != "":
                        for i in self.allViewElements:
                            i.undraw()
                        plane.passengerAccounts[newUsername] = newPassword
                        nextView = CategorySelectionView(self.win, newUsername, newPassword, plane, self.manager)
                        nextView.formatElements()
                        nextView.getButton()
                        self.formatElements()
                        self.newUserUsername.setText("")
                        self.newUserPassword.setText("")
                    else:
                        self.newUserText.setText("Please enter a valid password")
                else:
                    self.newUserText.setText("Please enter a valid username")
            if self.returnToAccountButton.clicked(p):
                for i in self.allViewElements:
                    i.undraw()
                status = False

    # ------------------------------------------------------------------
