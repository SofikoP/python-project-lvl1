from random import randint


game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'
greeting = 'Welcome to the Brain Games!'


def is_even(number):
    '''Checks if a number is even.
    '''

    return number % 2 == 0


def get_correct_answer(number):
    '''Returns 'yes' if a number is even and 'no' if isn`t.
    '''

    correct_answer = 'yes' if is_even(number) else 'no'
    return correct_answer


def play_even():
    print(greeting)
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_rule)
    counter = 0
    while counter != 3:
        random_number = randint(1, 101)
        print(f'Question: {random_number}')
        answer = input()
        correct_answer = get_correct_answer(random_number)
        if correct_answer == answer:
            counter += 1
            print('Correct!')
        else:
            return f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!"
    if counter == 3:
        return f'Congratulations, {name}!'
