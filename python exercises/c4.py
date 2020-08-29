import random

randNum = random.randint(1, 100)

if randNum < 50:
    print("Hint: Less than 50")
else:
    print("Hint: At least 50")

guessNumber = int(input("Guess the number: "))

if guessNumber is randNum:
    print("\nCongratulations you win :D")
else:
    print("\nSorry you lose :(\nThe real number is " + str(randNum))
