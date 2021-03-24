from random import randint

num = randint(1,10)
correct = False

while not correct:
  guess = int(input("Guess the number "))

  if guess == num:
    correct = True

print("Well done ya pleb")
