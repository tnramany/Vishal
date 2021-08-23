import random
print("let's guess a number between 1-20")

computer_no=random.randint(1,20)

guessesTaken= 0
score= 5

while guessesTaken<5:
    guess = int(input("What is your guess?"))

    guessesTaken= guessesTaken + 1

    if guess == computer_no:
        score = 5-guessesTaken
        s=str(score)

        print('You Win with a score of +5')

    elif guess>computer_no:
        print('Your guess is too high!')

    else:
        print('Your guess is too low!')

if guess == computer_no:

 print("Done")

else:
    print("You lose! The number is " + str(computer_no))