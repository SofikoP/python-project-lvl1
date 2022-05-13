from random import randint, choice


game_rule = 'What is the result of the expression?'


def get_question_answer():
    number_1 = randint(1, 51)
    number_2 = randint(1, 51)
    operation = choice('+-*')
    question = f'{number_1} {operation} {number_2}'
    if operation == '+':
        return question, str(number_1 + number_2)
    elif operation == '-':
        return question, str(number_1 - number_2)
    elif operation == '*':
        return question, str(number_1 * number_2)
