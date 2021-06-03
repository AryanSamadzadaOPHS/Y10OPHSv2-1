total, validTotal, invalidTotal = 0,0,0

while True:
  check = input("Do you want to check a UK phone Number? Y or N? ").upper()
  
  if check == "Y":
    total += 1
    num = input("Enter phone number: ")

    if num[0] == "0" and len(num) == 11:
      validTotal += 1
      print("\nValid UK phone number\n")
    
    else:
      invalidTotal += 1
      print("\nInvalid UK phone number\n")
    
  if check == "N":
    break

print(total, "numbers checked.\n")
print(validTotal, "numbers valid.\n")
print(invalidTotal, "numbers invalid.\n")
