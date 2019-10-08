
#
# userChoice = 0
#
#
# def start():
#     global userChoice
#     print("Welcome To Our Store.");
#     print("We had it developed by a discount developer so it might be a litle buggy.");
#     print("If you have any issues or need any help contact us @ nerd@columbusstate.edu\n\n");
#     print("Enter a number that matches your choice")
#     while userChoice != 1:
#         print("Register 1, Login 2, View Events 3, Purchase Tickets 4, Make A File 5, Run A File 6, Exit 7")
#         userChoice = input()
#         if userChoice == "7":
#             print("bye")
#             exit()
#         else:
#             print(userChoice)
#             print(" u wut")
#
#
# if __name__ == '__main__':
#     start();

startingPoints = 0
adminAccount = "admin"
adminPassword = "password"
ticketPointCost = 5
totalMoney = 100
userAccount = ""
userPassword = 853
userChoice = "0"
intUserChoice = 0

def start():
    global userChoice
    print("Welcome To Our Store.");
    print("We had it developed by a discount developer so it might be a litle buggy.");
    print("If you have any issues or need any help contact us @ nerd@columbusstate.edu\n\n");
    print("Enter a number that matches your choice")
    while userChoice != "7":
        print("Register 1, Login 2, View Events 3, Purchase Tickets 4, Make A File 5, Run A File 6, Exit 7")
        userChoice = input()
        intUserChoice = int(userChoice)
        if userChoice == "7":
            print("bye")
            exit()
        else:
            print(userChoice)
            print(" u wut")


if __name__ == '__main__':
    start()
