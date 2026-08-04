#Create a program that checks if a username exists in a predefined list of usernames. 
#Then, have the user input a password and check if it matches the password associated with that username. 
#Make sure that the program handles cases where the username does not exist, and where the password is incorrect.
#Give them 3 attempts to enter the correct password, and if they fail, lock them out of the system.

#list of usernames
usernames = ["Jack", "Alex", "Bob", "Max"]
#list of passwords
passwords = ["Money135", "Boxdragon853", "Vivensupporter1196", "Lover589"]
for x in range(3):
#tells them to Enter a username
      input_username = input("Enter a username: ")
      #looks for the username in the list
      for username in usernames:
            #if it is username
            if input_username == username:
                break
            else:
                  #write access denied
                  print("Access Denied")
                  #write locked out, please try again in 1 hour
print("locked out, please try again in 1 hour.")
#
for x in range (3):
      #password is input say enter a password
      password= input("enter a password: ")
      #if password is password
      for password in passwords:
            if password == passwords:
            #say access granted
                  print("Access Granted")
                  break
            else:
            #say access denied
                  print("Access Denied")
            #say locked out, please try again in 1 hour
print("locked out, please try again in 1 hour.")