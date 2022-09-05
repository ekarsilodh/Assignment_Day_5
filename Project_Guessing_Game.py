# Guessing game.
# 1. Python will guess a no. between 1 to 50.
# 2. Takes user input.
# 3. if the user input is near to 10 digits to the actual no. give 10 points
# 4. else if the user input is near to 5 digits to the actual no. give 25 points
# 5. else if the user input is the actual no. give 50 points
# 6. Show the output & score

import random

def guessgame():
    score = 0
    #generating the random no.
    actual_num = random.randint(1, 50)

    #taking user input
    user_num = input("Enter a no. between 1 to 50: ")

    #typecasting the input
    userNum = int(user_num)

    diff = actual_num - userNum

    #checking the difference
    if diff == 0:
        print("It's the same no. You get 50 points.")
        score = score + 50
        print("Your updated score is = ", score)

    elif abs(diff) <= 5:
        print("The no. is very close. You get 25 points.")
        print("Your input: ", userNum)
        print("Actual No. = ", actual_num)
        score = score + 25
        print("Your updated score is = ", score)

    elif abs(diff) <= 10 and abs(diff) > 5:
        print("The no. is close but not that much. You get 10 points.")
        print("Your input:", userNum)
        print("Actual No. =", actual_num)
        score = score + 10
        print("Your updated score is =", score)

    elif abs(diff) > 10:
        print("The no. is not close enough.")
        print("Your input:", userNum)
        print("Actual No. =", actual_num)
        score = score + 0
        print("Your updated score is =", score)

while True:
    print("To stop the game press enter.\n Else press Y.Y")
    a = input()

    if len(str(a)) == 0:
        break
    guessgame()