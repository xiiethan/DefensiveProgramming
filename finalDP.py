startingPoints = 0
## We're storing the adminAccount as hardcoded string.
## This will be easy to find even when the python is compiled into an executable.
adminAccount = "admin"
adminPassword = 1649 ## astrongpassword
accountArray = [adminAccount, "guest"]
passwordArray = {adminAccount: adminPassword, "guest": 883, "james":1236}
## The admin password is going to be a number which is weak aganist a keygen.

ticketPointCost = 5
totalMoney = 100
userAccount = ""
userPassword = 0
intUserChoice = 0

def userChoiceHandler(userChoice):
    if userChoice == "1":
        doThis()
    elif userChoice == "2":
        login()
    elif userChoice == "3":
        doThis()
    elif userChoice == "4":
        doThis()
    elif userChoice == "5":
        doThis()
    elif userChoice == "6":
        doThis()
    else:
        print("Please Enter A Valid Answer")


def doThis():
    print("should probably do this")

def login():
        print("Enter A User")
        user = input()
        if user in accountArray:
            print("Enter A Password")
            password = input()
            if passwordChecker(password, user):
                print("Welcome")
            else:
                print("Incorrect Password")
        else:
            print("We don't have that user please register.")


def passwordChecker(password, user):
    global passwordArray
    ## This loop takes the password variable and determines it's ascii value.
    sum = 0
    for i in password:
        sum += ord(i)
    ## print(sum)
    if passwordArray[user] == sum:
    ##    print("true")
        return True
    else:
    ##    print("false")
        return False

def start():
    userChoice = 0
    print("Welcome To Our Store.")
    print("We had it developed by a discount developer so it might be a litle buggy.")
    print("If you have any issues or need any help contact us @ nerd@columbusstate.edu\n\n")
    print("Enter a number that matches your choice")
    while userChoice != "7":
        print("Register 1, Login 2, View Events 3, Purchase Tickets 4, Make A File 5, Run A File 6, Exit 7")
        userChoice = input()
        intUserChoice = int(userChoice)
        if userChoice == "7":
            print("bye")
            exit()
        else:
            userChoiceHandler(userChoice)



if __name__ == '__main__':
    start()
