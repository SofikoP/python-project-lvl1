from random import randint


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_answer():
    question = randint(1, 100)
    answer = 'yes' if question % 2 == 0 else 'no'
    return question, answer
