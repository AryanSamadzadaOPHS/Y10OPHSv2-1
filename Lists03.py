nList = list()

while True:
    for i in range(3):
        names = input("Enter names of people you want to inv ")
        nList.append(names)

    loop = input("Invite more? y or n ").lower()

    if loop == "n":
        break
print(str(len(nList)) + " ppl inved")
