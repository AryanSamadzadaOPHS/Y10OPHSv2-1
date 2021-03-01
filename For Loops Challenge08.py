direction = input("Do you want to count up or down? Up or Down").lower()

if direction != "up" and direction != "down":
    print("I don't understand ")

if direction == "down":
    number = int(input("Enter a number below 20 "))
    for i in range(21 - number):
        print(20 - i)

if direction == "up":
    number = int(input("Enter a number"))
    for i in range(number):
        print(i + 1)
