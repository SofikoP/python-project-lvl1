from random import randint, choice


RULE = 'What is the result of the expression?'


def get_question_answer():
    number_1 = randint(1, 50)
    number_2 = randint(1, 50)
    operation = choice('+-*')
    question = f'{number_1} {operation} {number_2}'
    if operation == '+':
        answer = number_1 + number_2
    elif operation == '-':
        answer = number_1 - number_2
    elif operation == '*':
        answer = number_1 * number_2
    return question, str(answer)
