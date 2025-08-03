import random
def guess(x):
    print("Hey,This is a guessing game.You have to guess a number in the given range.\n Hope you will enjoy.Go break a leg.")
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess=int(input(f"Guess a number between 1 & {x}:"))
        if guess<random_number:
            print("Sorry, guess again. Too low!")
        elif guess>random_number:
            print("Sorry, guess again. Too high!")
    print(f"Yay!! Congrats...You have guessed the number {random_number} correctly.")

guess(100)


    
