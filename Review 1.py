import random
random_num = random.randint(0,100)
print("You have 1 try to guess the number I'm thinking of.")
guess = int(input("Enter your guess here: "))
if guess == random_num:
    print("You guessed it!")
elif guess > random_num:
    print("Too high.")
elif guess < random_num:
    print("Too low.")
