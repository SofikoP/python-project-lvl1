from random import randint


GAME_RULE = 'What number is missing in the progression?'
LEN_OF_PROGRESSION = 10


def get_question_answer():
    start = randint(1, 100)
    step = randint(1, 10)
    progression = []
    i = 0
    while i < LEN_OF_PROGRESSION:
        progression.append(str(start))
        start += step
        i += 1
    some_index = randint(0, 9)
    answer = progression[some_index]
    progression[some_index] = '..'
    question = ' '.join(progression)
    return question, answer
