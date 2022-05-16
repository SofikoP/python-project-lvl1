from random import randint


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    counter = 0
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            counter += 1
    return counter == 1


def get_question_answer():
    question = randint(1, 100)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer
