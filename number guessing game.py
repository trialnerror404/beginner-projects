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

def computer_guess (x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay, the computer guess your number: {guess} correctly!')

guess (10)