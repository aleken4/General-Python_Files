#Create a program that checks if a username exists in a predefined list of usernames. 
#Then, have the user input a password and check if it matches the password associated with that username. 
#Make sure that the program handles cases where the username does not exist, and where the password is incorrect.
#Give them 3 attempts to enter the correct password, and if they fail, lock them out of the system.

#list of usernames
data=[
      ["usernames:","passwords:"],
      ["Jack","Money135"],
      ["Alex","Boxdragon853"],
      ["Bob","Vivensupporter1196"],
      ["Max","Lover589"]
]

found_user = False
user_row = None
#list of passwords
for x in range(3):
#tells them to Enter a username
      input_username = input("Enter a username:")
      #looks for the username in the list
      for row in data:
            #if it is username
            if input_username == row[0]:
                found_user = True
                user_row = row
                break

      if found_user:
            break
      else:
                  #write access denied
                  print("Access Denied")
                  #write locked out, please try again in 1 hour
print("locked out, please try again in 1 hour.")
#
for x in range (3):
      #password is input say enter a password
      input_password= input("enter a password:")
      #if password is password
      for row in data:
            if input_password == user_row[1]:  # pyright: ignore[reportOptionalSubscript]
                 #say access granted
                 print("Access Granted")
                 break
            else:
            #say access denied
                 print("Access Denied")
      else:
            #say locked out, please try again in 1 hour
            print("locked out, please try again in 1 hour.")