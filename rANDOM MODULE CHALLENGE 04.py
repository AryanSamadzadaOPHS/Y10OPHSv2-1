from random import randint

num = randint(1,5)

for i in range(2):
  guess = int(input("guess the number "))

  if guess == num:
    print("U win")
    break
    
  if i == 1 and guess != num:
    print("U lose")
    break
