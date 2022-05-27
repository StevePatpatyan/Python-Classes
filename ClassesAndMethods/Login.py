from graphics import*
def Login(self,win,uFile,pFile,sFile):
    loggedIn = 0
    player = ["Player 1","Player 2"]
    user1Text = Text(Point(-1,-1),"null")
    #Sign in/log in
    while (True):
            userFile = open(uFile).read().split("\n")
            passFile = open(pFile).read().split("\n")
            scoreFile = open(sFile).read().split("\n")
            signIn = Rectangle(Point(400,100),Point(600,200))
            signInText = Text(Point(500,150),"Register Username")
            logIn = Rectangle(Point(400,225),Point(600,325))
            logInText = Text(Point(500,275),"Log In As An Existing User")
            signIn.draw(win)
            signInText.draw(win)
            logIn.draw(win)
            logInText.draw(win)
            while (True):
                    logButton = win.getMouse()
                    if (logButton.getX()>=signIn.getP1().getX() and logButton.getX()<=signIn.getP2().getX() and logButton.getY()>=signIn.getP1().getY() and logButton.getY()<=signIn.getP2().getY()):
                            logVal = 0
                            break
                    elif (logButton.getX()>=logIn.getP1().getX() and logButton.getX()<=logIn.getP2().getX() and logButton.getY()>=logIn.getP1().getY() and logButton.getY()<=logIn.getP2().getY()):
                            logVal = 1
                            break
            signIn.undraw()
            signInText.undraw()
            logIn.undraw()
            logInText.undraw()
            logTextStatus = ["Register As A New Player:","Log In As "+player[loggedIn]+":"]
            logText = Text(Point(500,50),logTextStatus[logVal])
            userEnter = Entry(Point(500,200),50)
            userEnterText = Text(Point(500,175),"Username:")
            passEnter = Entry(Point(500,300),50)
            passEnterText = Text(Point(500,275),"Password:")
            confirmLog = Rectangle(Point(400,350),Point(600,450))
            confirmLogText = Text(Point(500,400),"Confirm")
            logText.draw(win)
            userEnter.draw(win)
            userEnterText.draw(win)
            passEnter.draw(win)
            passEnterText.draw(win)
            confirmLog.draw(win)
            confirmLogText.draw(win)
            errorText = 0
            wait = True
            while (True):
                    userButton = win.getMouse()
                    if (userButton.getX()>=confirmLog.getP1().getX() and userButton.getX()<=confirmLog.getP2().getX() and userButton.getY()>=confirmLog.getP1().getY() and userButton.getY()<=confirmLog.getP2().getY()):                      
                            if (errorText!=0):
                                    errorText.undraw()
                            for users in range(len(userFile)):
                                    if (logVal==0):
                                            if (userEnter.getText()==""):
                                                    errorText = Text(Point(500,475),"Username required")
                                                    errorText.setFill("red")
                                                    errorText.draw(win)
                                                    break
                                            elif (passEnter.getText()==""):
                                                    errorText = Text(Point(500,475),"Password required")
                                                    errorText.setFill("red")
                                                    errorText.draw(win)
                                                    break
                                            elif (userEnter.getText()== userFile[users]):
                                                    errorText = Text(Point(500,475),"Username already registered")
                                                    errorText.setFill("red")
                                                    errorText.draw(win)
                                                    break
                                            elif (users == len(userFile)-1):
                                                    open(uFile,"a").write(userEnter.getText()+"\n")
                                                    open(pFile,"a").write(passEnter.getText()+"\n")
                                                    open(sFile,"a").write("0-0-0\n")
                                                    userFile = open(uFile).read().split("\n")
                                                    passFile = open(pFile).read().split("\n")
                                                    scoreFile = open(sFile).read().split("\n")
                                                    errorText = Text(Point(500,475),"Successfully registered account")
                                                    errorText.setFill("light green")
                                                    errorText.draw(win)
                                                    wait = False
                                                    time.sleep(1)
                                    elif (logVal==1):
                                            if (userEnter.getText()==""):
                                                    errorText = Text(Point(500,475),"Username required")
                                                    errorText.setFill("red")
                                                    errorText.draw(win)
                                                    break
                                            elif (passEnter.getText()==""):
                                                    errorText = Text(Point(500,475),"Password required")
                                                    errorText.setFill("red")
                                                    errorText.draw(win)
                                                    break
                                            elif (userEnter.getText()==userFile[users] and passEnter.getText()!=passFile[users]):
                                                    errorText = Text(Point(500,475),"Username or password does not match")
                                                    errorText.setFill("red")
                                                    errorText.draw(win)
                                                    break
                                            elif (userEnter.getText()==userFile[users] and passEnter.getText()==passFile[users]):
                                                    if (userEnter.getText()==user1Text.getText()):
                                                            errorText = Text(Point(500,475),"Username already logged in as Player 1")
                                                            errorText.setFill("blue")
                                                            errorText.draw(win)
                                                            break
                                                    else:
                                                            errorText = Text(Point(500,475),"Logged in successfully")
                                                            errorText.setFill("light green")
                                                            if (loggedIn==0):
                                                                    self.user1Text = Text(Point(400,340),userFile[users])
                                                                    self.score1Text = Text(Point(30,490),scoreFile[users])
                                                            elif (loggedIn==1):
                                                                    self.user2Text = Text(Point(600,340),userFile[users])
                                                                    self.score2Text = Text(Point(970,490),scoreFile[users])
                                                            errorText.draw(win)
                                                            loggedIn = loggedIn+1
                                                            wait = False
                                                            time.sleep(1)
                                                            break
                                            elif (users == len(userFile)-1):
                                                    errorText = Text(Point(500,475),"Username does not exist")
                                                    errorText.setFill("red")
                                                    errorText.draw(win)
                                                    break
                            users = 0
                            if (wait==False):
                                    logText.undraw()
                                    userEnter.undraw()
                                    userEnterText.undraw()
                                    passEnter.undraw()
                                    passEnterText.undraw()
                                    confirmLog.undraw()
                                    confirmLogText.undraw()
                                    errorText.undraw()
                                    break
            if (wait==False and logVal==1 and loggedIn==2):
                    break
