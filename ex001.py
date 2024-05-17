import random

def guess(x): 
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Digite um numero entre 1 e {x}: '))
        print(guess)
        if guess < random_number:
            print('Sorry, guess again. Too low')
        elif guess > random_number: 
            print('Sorry, guess again. Too high')
            
    print(f'Yay, congrats. You have guessed the number {random_number} correcly!!')
    

guess(10)