import prompt


def enter_name():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name
