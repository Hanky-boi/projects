import random
def numgus():
    number = random.randint(1, 10)
    guesslist = []
    attempts = 1
    guess = None
    while guess != number:
        guess = int(input("Guess a number between 1 and 10: "))
        guesslist.append(guess)
        if guess < number:
            print("Too low folk")
            attempts += 1
        elif guess > number:
            print("Too high pal")
            attempts += 1
    print(f"gg, u guessed the number in {attempts} attempts and used numbers {guesslist}")
numgus()