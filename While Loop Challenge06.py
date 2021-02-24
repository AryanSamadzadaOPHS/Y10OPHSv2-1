num = int(input("Enter a number between 10 and 20"))

while not 10 <= num <= 20:
    if num > 20:
        print("Too high")
    if num < 10:
        print("Too low")

    num = int(input("Try again "))

print("Thx")
