import prompt


NUMBER_OF_TRY = 3


def play_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_RULE)
    counter = 0
    while counter != NUMBER_OF_TRY:
        (question, answer) = game.get_question_answer()
        print(f'Question: {question}')
        user_answ = prompt.string('Your answer: ')
        wrong_answer = (
            f"'{user_answ}' is wrong answer ;(. Correct answer was '{answer}'."
            f"\nLet's try again, {name}!"
        )
        if user_answ == answer:
            print('Correct!')
            counter += 1
        else:
            return wrong_answer
    if counter == NUMBER_OF_TRY:
        return f'Congratulations, {name}!'
