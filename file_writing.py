#Code to write to file

try:
    file = open("users_info.txt", "w")
except:
    print("Couldn't open specified file.")

user = input("Write to file: ")
#file.write(user.password + "\n")
file.write(users_info.txt)
file.close()

##Code to open the file for testing
##try:
##    file = open("users_info.txt", "r")
##except:
##    print("Couldn't open specified file.")
##    
##    
##print(file.read())
##
##file.close()
