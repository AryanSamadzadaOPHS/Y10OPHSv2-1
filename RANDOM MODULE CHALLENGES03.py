from random import choice

coin = choice(["Heads", "Tails"])
guess = input("Heads or tails? ").lower()

print("It was " + coin)

if guess == coin.lower():
    print("u win")

else:
    print("L u lose")
