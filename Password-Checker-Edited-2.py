data = [
    ["usernames:", "passwords:"],
    ["Jack", "Money135"],
    ["Alex", "Boxdragon853"],
    ["Bob", "Vivensupporter1196"],
    ["Max", "Lover589"]
]

# username attempts
found_user = False
user_row = None

for x in range(3):
    input_username = input("Enter a username: ")

    for row in data:
        if input_username == row[0]:
            found_user = True
            user_row = row
            break

    if found_user:
        break
    else:
        print("Access Denied")

if not found_user:
    print("Locked out, please try again in 1 hour.")

else:
    # password attempts
    for x in range(3):
        input_password = input("Enter a password: ")

        if input_password == user_row[1]:
            print("Access Granted")
            break
        else:
            print("Access Denied")
    else:
        print("Locked out, please try again in 1 hour.")
