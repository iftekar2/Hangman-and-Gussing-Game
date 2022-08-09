import random 

message = int(input("1. If you want to guess a number. 2. If you want the computer to guess a number: "))
if message == 1:
    def guess(x):
        random_number = random.randint(1, x)
        guess = 0
        while guess != random_number:
            guess = int(input(f"Guess a number between 1 and {x}: "))
            if guess < random_guess:
                print("Your guess is too high")
            elif guess > random_guess:
                print("Your guess is too low")
        print("You guessed correct")
    guess(10)
elif message == 2:
    def random_guess(x):
        low = 1
        high = x
        feedback = ''
        while feedback != "c":
            if low != high:
                guess = random.randint(low, high)
            else: 
                guess = low
            feedback = input(f"Is {guess} too high(h) or is it too low(l) or is it correct(c): ")
            if feedback == 'h':
                high = guess - 1
            elif feedback == 'l':
                low = guess + 1
        print("I have guessed correct")
    random_guess(10)