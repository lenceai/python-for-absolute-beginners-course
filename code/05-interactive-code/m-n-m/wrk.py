import random

print('Hellow World')
print('M&M Guessing gamel')

mm_count = random.randint(1, 100)

print('Guess the numver')
attempt_limit = 7
attempts = 0

while attempts < attempt_limit:
    guess_text = input('How many MM are their in the jar ')
    guess = int(guess_text)

    if mm_count == guess:
        print(f'You get free lunch {guess}.')
        break
    elif guess < mm_count:
        print('Sorry, to low')
    else:
        print('that is to high')

    attempts += 1

print('Bye')
