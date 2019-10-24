import random

guess = input('Pick a number between 1 and 10')
guess = int(guess)
print(guess)

hidden = random.randint(1, 10)

if hidden == guess:
    print('Correct')
elif guess < hidden:
    print('Your guess is too low')
else:
    print('Your guess is too high')