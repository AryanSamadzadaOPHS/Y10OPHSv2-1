total = 0

for i in range(5):
    num = int(input("Enter a number "))
    add = input("Do you want to add this number? Y or N ").lower()

    if add == "y":
        total += num

print(total)
