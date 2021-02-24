compNum = 50
num = int(input("Enter a number"))
count = 1

while num != 50:
    if num < 50:
        print("Low")
    if num > 50:
        print("High")
    num = int(input("Have another guess"))
    count += 1

print(f"Well done you took {count} attempts")
