
Tv = ["Attack on Titan", "Tokyo Ghoul", "Seven Deadly Sins", "One piece"]

for i in Tv:
    print(i)

show = str(input("Enter another show "))
pos = int(input("What position you want it? eg: 1,2,3... ")) - 1

Tv.insert(pos, show)

for i in Tv:
    print(i)

