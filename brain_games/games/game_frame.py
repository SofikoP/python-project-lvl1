number_of_try = 3


def play_game(game):
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.game_rule)
    counter = 0
    while counter != number_of_try:
        (question, answer) = game.get_question_answer()
        print(f'Question: {question}')
        user_answ = input('Your answer: ')
        wrong_answer = (
            f"'{user_answ}' is wrong answer ;(. Correct answer was '{answer}'."
            f"\nLet's try again, {name}!"
        )
        if user_answ == answer:
            print('Correct!')
            counter += 1
        else:
            return wrong_answer
    if counter == number_of_try:
        return f'Congratulations, {name}!'
