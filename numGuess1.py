import random

computer_no=random.randint(1,20)

def sameno(target,number):

    if target == number:
      result = "Win"
    elif target>number:
      result="Low"
    else:
        result="high"

    return result

print("Guess a number between 1-20")

guess=int(input("What is your guess?"))

print(sameno(computer_no,guess))

high_or_low=sameno(computer_no,guess)

while high_or_low != "Win":
    if high_or_low == "low":
        guess=int(input("Too Low. Try again"))

    else:
        guess = int(input("Too high. Try again"))

    high_or_low = sameno(computer_no, guess)

input("Exit")

