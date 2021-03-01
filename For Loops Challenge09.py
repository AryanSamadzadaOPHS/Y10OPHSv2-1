num = int(input("How many ppl do u want to invite? "))

if num >= 10:
    print("Too many people")

if num < 10:
    for i in range(num):
        name = input("Who do you want to invite ")
        print(name + " has been invited")
