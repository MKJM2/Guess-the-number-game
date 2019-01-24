import random

answer = input('Hello there! Shall we start the game? (Y/N)')
def start(answer):

    answer.upper()
    if answer == 'N':
        exit()
    elif answer == 'Y':
        main()
    else:
        answer = input('Yes or No???')
        start()

def compare(guess, number):
    if guess < number:
        print('Too small!')
        return False
    elif guess > number:
        print('Too large!')
        return False
    elif guess == number:
        return True


def main():
    min_value = 0
    max_value = 10
    guesses = 0
    equal = 0;

    number = random.randint(min_value, max_value)
    print('I have chosen a random number between {} and {}'.format(min_value, max_value))
    guess = int(input('Now try to guess it! : '))
    guesses = guesses + 1
    equal = compare(guess, number)

    while equal == False:
        print('Try again.')
        guess = int(input())
        guesses = guesses + 1

        equal = compare(guess, number)


    print('Congrats! You guessed it right! It took you {} tries'.format(guesses))


start(answer)
