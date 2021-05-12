food = []

for i in range(4):
    f = input("Give a food ")
    food.append(f)
print(food)

for i in range(2):
    delete = int(input("Which food to delete? ")) - 1
    food.remove(food[delete])
    print(food)
    
