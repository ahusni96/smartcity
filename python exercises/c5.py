import random

randNum = random.randint(1, 100)
print(randNum)

guessNum = 0

while guessNum is not randNum:
    guessNum = input("Enter a number: ")

    if not guessNum.isnumeric():
        print("Not a number")
        continue
    else:
        guessNum = int(guessNum)
        
        if guessNum < randNum:
            print("Low")
        elif guessNum is randNum:
            print("You are correct =D")
        else:
            print("High")
