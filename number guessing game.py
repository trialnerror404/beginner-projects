import random

def guess(x):
    random_number = random.randint(1,x)
    # guess will not = the numer
    guess = 0
    # want to keep guessing when
    # the input number does not equal to the actual number
    while guess !=  random_number:
        guess = int(input(f'Guess a number between 1 to {x}: '))
        if guess < random_number:
            print("Sorry, please guess again. Too Low")
        elif guess > random_number:
            print("Sorry, please guess again, Too High")
        elif guess == random_number:
            print (f"Yay, you have got the correct number {random_number}")
            break
guess(10)
