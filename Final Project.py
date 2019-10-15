#Ethan Dillinger

class user:

    def __init__ (self, defined_username, defined_password):
        self.username = defined_username
        self.password = defined_password


class interface:


    def events():
        print("MarioKart Tournament on Monday\nAnime Night on Tuesday\nMovie night on Friday\nConcert on Saturday")

    def account():
        x = int(input("(1)Log in\n(2)Create account"))
        if (x == 1):
            

            
        if (x == 2):
            defined_username = input("Enter username: ")
            defined_password = input("Enter password: ")
            #Encrypt and store in file

    def ticketpurchase():
        choice = int(input("Which event would you like to purchase a ticket to?\n(1)MarioKart Tournament on Monday\n(2)Anime Night on Tuesday\n(3)Movie night on Friday\n(4)Concert on Saturday"))
        if (choice == 1):
            ticket_amount = int(input("How many tickets? "))
            card = input("Enter 16 digit card number: ")
        

    def main():
        #MENU
        int choice = 0
        while (choice != 4):
            choice = int(input("(1) View Events\n(2) Log in/Create account\n(3) Purchase Tickets\n(4) Exit")
                     
            if (choice == 1):
                events()
            elif (choice == 2):
                account()
            elif (choice == 3)
                ticketpurchase()
            


    main()
