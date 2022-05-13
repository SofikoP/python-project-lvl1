from random import randint


game_rule = 'Find the greatest common divisor of given numbers.'


def get_question_answer():
    number_1 = randint(1, 101)
    number_2 = randint(1, 101)
    question = f'{number_1} {number_2}'
    while number_1 != 0 and number_2 != 0:
        if number_1 > number_2:
            number_1 = number_1 % number_2
        else:
            number_2 = number_2 % number_1
    answer = str(number_1 + number_2)
    return question, answer
