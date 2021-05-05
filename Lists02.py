cars = []
end = False

while not end:
    car = input("Enter brand ").lower()
    cars.append(car)

    if car == "x":
        end = True
        

print("Exiting")
print("The list is " , cars)
