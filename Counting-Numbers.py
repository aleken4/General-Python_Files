#asks the user for a number, then counts up to that number, and then to 0

Number=int(input("Write a number: "))
for x in range(0,Number+1):
    print(x)
for x in range(0,Number+1):
    print(Number-x)