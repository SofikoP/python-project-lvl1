from random import randint
from math import sqrt


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def get_question_answer():
    question = randint(1, 100)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer
