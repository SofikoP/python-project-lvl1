from random import randint


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    divisor = 2
    while number % divisor != 0:
        divisor += 1
    return divisor == number


def get_question_answer():
    question = randint(1, 100)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer
