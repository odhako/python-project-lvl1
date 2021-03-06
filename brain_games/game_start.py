import prompt

ROUNDS_COUNT = 3


def game_start(rules, round_generator):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(rules)
    i = 0
    while i < ROUNDS_COUNT:
        question, right_answer = round_generator()
        if right_answer == 'Error':
            raise AssertionError('Invalid quiestion')
        print('Question: ' + question)
        answer = str.lower(prompt.string('Your answer: '))
        if answer == right_answer:
            print('Correct!')
            i += 1
        else:
            print(f"{answer} is wrong answer ;(. "
                  f"Correct answer was {right_answer}")
            print(f"Let's try again, {name}!")
            break
    else:
        print('Congratulations, ' + name + '!')
