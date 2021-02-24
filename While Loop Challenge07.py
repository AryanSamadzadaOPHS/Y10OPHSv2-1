bottles = 10

while bottles != 0:
    print(f"“There are {bottles} green bottles hanging on the wall, {bottles} green bottles hanging on the wall, And if one green bottle should accidentally fall")
    ans = int(input("How many green bottles on the wall? "))
    bottles -= 1

    while ans != bottles:
        print("Wrong try again")
        ans = int(input("How many green bottles on the wall? "))
