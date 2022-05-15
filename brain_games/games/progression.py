from random import randint


game_rule = 'What number is missing in the progression?'
len_of_progression = 10


def get_question_answer():
    start = randint(1, 100)
    step = randint(1, 10)
    progression = []
    i = 0
    while i < len_of_progression:
        progression.append(str(start))
        start += step
        i += 1
    some_index = randint(0, 9)
    answer = progression[some_index]
    progression[some_index] = '..'
    question = ' '.join(progression)
    return question, answer
